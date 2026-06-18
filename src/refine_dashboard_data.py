import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASHBOARD_DIR = os.path.join(BASE_DIR, 'dashboard')

def clean_dashboard_csv():
    input_path = os.path.join(DASHBOARD_DIR, 'powerbi_or_tableau_data.csv')
    output_path = os.path.join(DASHBOARD_DIR, 'student_success_dashboard_clean.csv')
    
    if not os.path.exists(input_path):
        print("Error: Input CSV not found.")
        return
        
    df = pd.read_csv(input_path)
    
    # 1. Fill missing categories with 'Unknown'
    df['intervention_type'] = df['intervention_type'].fillna('No Intervention')
    df['placement_language'] = df['placement_language'].fillna('None')
    
    # 2. Ensure Risk Category is ordered
    risk_order = ['Low Risk', 'Medium Risk', 'High Risk']
    df['risk_category'] = pd.Categorical(df['risk_category'], categories=risk_order, ordered=True)
    
    # 3. Boolean to Yes/No where useful
    # Already Yes/No in most cases from previous script, but let's be sure
    bool_cols = ['international_student', 'first_generation', 'retake_required', 'has_hold', 'unresolved_hold_flag', 'intervention_received_flag', 'enrolled_flag', 'completed_flag', 'enrollment_delay_flag']
    for col in bool_cols:
        if df[col].dtype == bool:
            df[col] = df[col].map({True: 'Yes', False: 'No'})

    # 4. Numeric formatting (ensure no weird floats where integers expected)
    df['total_test_attempts'] = df['total_test_attempts'].fillna(0).astype(int)
    df['latest_placement_score'] = df['latest_placement_score'].fillna(0)
    df['at_risk_score'] = df['at_risk_score'].astype(int)
    df['student_id'] = df['student_id'].astype(int)
    df['age'] = df['age'].astype(int)
        
    df.to_csv(output_path, index=False)
    print(f"Cleaned dashboard CSV saved to {output_path}")

if __name__ == "__main__":
    clean_dashboard_csv()
