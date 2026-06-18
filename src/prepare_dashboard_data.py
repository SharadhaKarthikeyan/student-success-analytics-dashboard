import pandas as pd
import numpy as np
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNTHETIC_DIR = os.path.join(BASE_DIR, 'data', 'synthetic')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
DASHBOARD_DIR = os.path.join(BASE_DIR, 'dashboard')

os.makedirs(DASHBOARD_DIR, exist_ok=True)

def prepare_dashboard_csv():
    # Load data
    students = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'students.csv'))
    placement = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'placement_tests.csv'))
    holds = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'enrollment_holds.csv'))
    interventions = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'advising_interventions.csv'))
    courses = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'course_enrollment.csv'))
    risk_df = pd.read_csv(os.path.join(PROCESSED_DIR, 'student_risk_analysis.csv'))

    # Aggregations for joining
    # Placement
    latest_placement = placement.sort_values(['student_id', 'test_date']).groupby('student_id').tail(1)
    latest_placement = latest_placement.rename(columns={'score': 'latest_placement_score', 'language': 'placement_language'})
    
    total_attempts = placement.groupby('student_id')['attempt_number'].max().reset_index()
    total_attempts.columns = ['student_id', 'total_test_attempts']
    
    retake_req = placement.groupby('student_id')['retake_required'].apply(lambda x: 'Yes' if 'Yes' in x.values else 'No').reset_index()
    
    # Holds
    has_hold = holds.groupby('student_id')['hold_id'].count().reset_index()
    has_hold['has_hold'] = 'Yes'
    
    unresolved_hold = holds[holds['status'] == 'Active'].groupby('student_id')['hold_id'].count().reset_index()
    unresolved_hold['unresolved_hold_flag'] = 'Yes'
    
    avg_hold_days = holds.groupby('student_id')['days_to_resolve'].mean().reset_index()
    avg_hold_days.columns = ['student_id', 'avg_days_to_resolve_hold']
    
    # Interventions
    received_int = interventions.groupby('student_id')['intervention_id'].count().reset_index()
    received_int['intervention_received_flag'] = 'Yes'
    
    latest_int = interventions.sort_values(['student_id', 'intervention_date']).groupby('student_id').tail(1)
    latest_int = latest_int[['student_id', 'intervention_type']]
    
    # Enrollment/Courses
    enrolled_stat = courses.groupby('student_id')['enrolled_flag'].apply(lambda x: 'Yes' if 'Yes' in x.values else 'No').reset_index()
    completed_stat = courses.groupby('student_id')['completed_flag'].apply(lambda x: 'No' if 'No' in x.values else 'Yes').reset_index()

    # Base Join
    df = students.merge(risk_df[['student_id', 'at_risk_score', 'risk_category', 'at_risk_flag']], on='student_id', how='left')
    
    # Add Placement info
    df = df.merge(latest_placement[['student_id', 'latest_placement_score', 'placement_language']], on='student_id', how='left')
    df = df.merge(total_attempts, on='student_id', how='left')
    df = df.merge(retake_req, on='student_id', how='left')
    
    # Add Hold info
    df = df.merge(has_hold[['student_id', 'has_hold']], on='student_id', how='left').fillna({'has_hold': 'No'})
    df = df.merge(unresolved_hold[['student_id', 'unresolved_hold_flag']], on='student_id', how='left').fillna({'unresolved_hold_flag': 'No'})
    df = df.merge(avg_hold_days, on='student_id', how='left')
    
    # Add Intervention info
    df = df.merge(received_int[['student_id', 'intervention_received_flag']], on='student_id', how='left').fillna({'intervention_received_flag': 'No'})
    df = df.merge(latest_int, on='student_id', how='left')
    
    # Add Enrollment info
    df = df.merge(enrolled_stat, on='student_id', how='left')
    df = df.merge(completed_stat, on='student_id', how='left')
    
    # Derived columns
    df['placement_score_band'] = pd.cut(df['latest_placement_score'], bins=[0, 60, 80, 100], labels=['Low', 'Medium', 'High'])
    
    def hold_res_cat(days):
        if pd.isna(days): return 'No Hold'
        if days <= 7: return 'Quick (<=7 days)'
        if days <= 14: return 'Moderate (8-14 days)'
        return 'Slow (>14 days)'
    df['hold_resolution_category'] = df['avg_days_to_resolve_hold'].apply(hold_res_cat)
    
    df['enrollment_delay_flag'] = df.apply(lambda x: 'Yes' if x['unresolved_hold_flag'] == 'Yes' or x['avg_days_to_resolve_hold'] > 14 else 'No', axis=1)

    # Final selection and cleaning
    output_path = os.path.join(DASHBOARD_DIR, 'powerbi_or_tableau_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Dashboard-ready CSV saved to {output_path}")

if __name__ == "__main__":
    print("Preparing dashboard data...")
    prepare_dashboard_csv()
    print("Dashboard data preparation completed!")
