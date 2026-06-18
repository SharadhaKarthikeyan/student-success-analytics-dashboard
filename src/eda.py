import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNTHETIC_DIR = os.path.join(BASE_DIR, 'data', 'synthetic')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
VISUALS_DIR = os.path.join(BASE_DIR, 'visuals')

os.makedirs(VISUALS_DIR, exist_ok=True)

def load_data():
    students = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'students.csv'))
    placement = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'placement_tests.csv'))
    holds = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'enrollment_holds.csv'))
    interventions = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'advising_interventions.csv'))
    courses = pd.read_csv(os.path.join(SYNTHETIC_DIR, 'course_enrollment.csv'))
    return students, placement, holds, interventions, courses

def apply_risk_logic(students, placement, holds, interventions, courses):
    # Prepare aggregation for risk scoring
    # 1. Unresolved hold flag
    unresolved_holds = holds[holds['status'] == 'Active'].groupby('student_id')['hold_id'].count().reset_index()
    unresolved_holds.columns = ['student_id', 'unresolved_hold_count']
    
    # 2. Latest placement score < 60
    latest_placement = placement.sort_values(['student_id', 'test_date']).groupby('student_id').tail(1)
    
    # 3. Retake required (more than 1 attempt)
    test_attempts = placement.groupby(['student_id', 'language'])['attempt_number'].max().reset_index()
    students_with_retakes = test_attempts[test_attempts['attempt_number'] > 1]['student_id'].unique()
    
    # 4. Intervention received flag (did NOT receive intervention)
    received_intervention = interventions['student_id'].unique()
    
    # 5. Enrollment delay (Synthetic rule: had a hold longer than 15 days or unresolved)
    delayed_students = holds[(holds['days_to_resolve'] > 15) | (holds['status'] == 'Active')]['student_id'].unique()
    
    # Merge risk factors into students df
    risk_df = students.copy()
    risk_df = risk_df.merge(unresolved_holds, on='student_id', how='left').fillna(0)
    risk_df = risk_df.merge(latest_placement[['student_id', 'score']], on='student_id', how='left')
    
    # Risk Conditions
    # - GPA band is Low
    risk_df['risk_gpa'] = (risk_df['gpa_band'] == 'Low').astype(int)
    # - Unresolved enrollment hold
    risk_df['risk_hold'] = (risk_df['unresolved_hold_count'] > 0).astype(int)
    # - Placement score is below 60
    risk_df['risk_placement_score'] = (risk_df['score'] < 60).astype(int)
    # - Student required more than one test attempt
    risk_df['risk_retake'] = risk_df['student_id'].isin(students_with_retakes).astype(int)
    # - Student did not receive advising intervention
    risk_df['risk_no_intervention'] = (~risk_df['student_id'].isin(received_intervention)).astype(int)
    # - Student has enrollment delay
    risk_df['risk_delay'] = risk_df['student_id'].isin(delayed_students).astype(int)
    # - Student status is Dropout or Enrolled instead of Graduate
    risk_df['risk_status'] = risk_df['student_status'].isin(['Dropout', 'Enrolled']).astype(int)
    
    risk_cols = ['risk_gpa', 'risk_hold', 'risk_placement_score', 'risk_retake', 'risk_no_intervention', 'risk_delay', 'risk_status']
    risk_df['at_risk_score'] = risk_df[risk_cols].sum(axis=1)
    risk_df['at_risk_flag'] = (risk_df['at_risk_score'] >= 2).astype(int)
    
    def category_risk(score):
        if score <= 1: return 'Low Risk'
        if score <= 3: return 'Medium Risk'
        return 'High Risk'
    
    risk_df['risk_category'] = risk_df['at_risk_score'].apply(category_risk)
    
    return risk_df

def create_visuals(students, placement, holds, interventions, courses, risk_df):
    # 1. dropout_distribution.png
    plt.figure(figsize=(10, 6))
    status_counts = students['student_status'].value_counts()
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Student Status Distribution')
    plt.savefig(os.path.join(VISUALS_DIR, 'dropout_distribution.png'))
    plt.close()
    
    # 2. graduation_rate_by_group.png
    plt.figure(figsize=(12, 6))
    grad_rate = students.groupby('gpa_band')['student_status'].apply(lambda x: (x == 'Graduate').mean()).reset_index()
    sns.barplot(data=grad_rate, x='gpa_band', y='student_status', palette='viridis')
    plt.title('Graduation Rate by GPA Band')
    plt.ylabel('Graduation Rate')
    plt.savefig(os.path.join(VISUALS_DIR, 'graduation_rate_by_group.png'))
    plt.close()
    
    # 3. placement_test_performance.png
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=placement, x='language', y='score', hue='attempt_number')
    plt.title('Placement Test Scores by Language and Attempt')
    plt.savefig(os.path.join(VISUALS_DIR, 'placement_test_performance.png'))
    plt.close()
    
    # 4. enrollment_hold_resolution.png
    plt.figure(figsize=(12, 6))
    avg_hold_time = holds.groupby('hold_type')['days_to_resolve'].mean().reset_index()
    sns.barplot(data=avg_hold_time, x='hold_type', y='days_to_resolve', palette='magma')
    plt.title('Average Days to Resolve Holds by Hold Type')
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(VISUALS_DIR, 'enrollment_hold_resolution.png'))
    plt.close()
    
    # 5. intervention_outcomes.png
    plt.figure(figsize=(12, 6))
    sns.countplot(data=interventions, x='intervention_type', hue='outcome', palette='Set2')
    plt.title('Advising Intervention Outcomes')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(VISUALS_DIR, 'intervention_outcomes.png'))
    plt.close()
    
    print("Visuals saved to visuals/ directory.")

if __name__ == "__main__":
    print("Starting EDA...")
    s, p, h, i, c = load_data()
    risk_df = apply_risk_logic(s, p, h, i, c)
    create_visuals(s, p, h, i, c, risk_df)
    
    # Save risk analysis for dashboard prep
    risk_df.to_csv(os.path.join(PROCESSED_DIR, 'student_risk_analysis.csv'), index=False)
    print("EDA completed and risk analysis saved.")
