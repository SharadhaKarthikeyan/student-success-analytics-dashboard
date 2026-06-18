import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNTHETIC_DIR = os.path.join(BASE_DIR, 'data', 'synthetic')
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')

os.makedirs(SYNTHETIC_DIR, exist_ok=True)
os.makedirs(RAW_DIR, exist_ok=True)

def generate_students(n=3000):
    majors = ['Computer Science', 'Business Administration', 'Nursing', 'Psychology', 'Mechanical Engineering', 'Education', 'Biology', 'Architecture']
    class_levels = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    admission_terms = ['Fall 2022', 'Spring 2023', 'Fall 2023', 'Spring 2024']
    gpa_bands = ['High', 'Medium', 'Low']
    statuses = ['Dropout', 'Enrolled', 'Graduate']
    
    student_ids = [1000 + i for i in range(n)]
    
    data = {
        'student_id': student_ids,
        'age': np.random.randint(18, 35, size=n),
        'gender': np.random.choice(['Male', 'Female', 'Non-binary'], size=n),
        'major': np.random.choice(majors, size=n),
        'class_level': np.random.choice(class_levels, size=n),
        'international_student': np.random.choice(['Yes', 'No'], size=n, p=[0.15, 0.85]),
        'first_generation': np.random.choice(['Yes', 'No'], size=n, p=[0.4, 0.6]),
        'admission_term': np.random.choice(admission_terms, size=n),
        'academic_standing': np.random.choice(['Good Standing', 'Probation', 'Warning'], size=n, p=[0.8, 0.15, 0.05]),
        'gpa_band': np.random.choice(gpa_bands, size=n, p=[0.3, 0.5, 0.2]),
        'student_status': np.random.choice(statuses, size=n, p=[0.2, 0.3, 0.5])
    }
    
    # Logic: Lower GPA students more likely to be Dropouts
    df = pd.DataFrame(data)
    df.loc[df['gpa_band'] == 'Low', 'student_status'] = np.random.choice(['Dropout', 'Enrolled'], size=len(df[df['gpa_band'] == 'Low']), p=[0.6, 0.4])
    
    df.to_csv(os.path.join(SYNTHETIC_DIR, 'students.csv'), index=False)
    return student_ids, df

def generate_placement_tests(student_ids):
    languages = ['English', 'Spanish', 'Math']
    test_rows = []
    
    test_id_counter = 5000
    for sid in student_ids:
        for lang in languages:
            # 80% take the test
            if random.random() > 0.2:
                attempts = 1
                if random.random() > 0.7: # 30% need retake
                    attempts = 2
                
                for att in range(1, attempts + 1):
                    score = np.random.randint(40, 100)
                    if att == 1 and score < 60:
                        passed = False
                        retake = True
                    else:
                        passed = True
                        retake = False
                        
                    placement_level = 'Advanced' if score > 85 else 'Intermediate' if score > 70 else 'Beginner'
                    
                    test_rows.append({
                        'test_id': test_id_counter,
                        'student_id': sid,
                        'language': lang,
                        'test_date': (datetime(2023, 8, 1) + timedelta(days=np.random.randint(0, 30))).strftime('%Y-%m-%d'),
                        'score': score,
                        'placement_level': placement_level,
                        'attempt_number': att,
                        'passed_flag': 'Yes' if passed else 'No',
                        'retake_required': 'Yes' if retake else 'No'
                    })
                    test_id_counter += 1
                    if passed: break # stop if passed
                    
    df = pd.DataFrame(test_rows)
    df.to_csv(os.path.join(SYNTHETIC_DIR, 'placement_tests.csv'), index=False)
    return df

def generate_enrollment_holds(student_ids):
    hold_types = ['Financial', 'Academic Advising', 'Immunization', 'Transcript', 'Disciplinary']
    hold_rows = []
    
    hold_id_counter = 8000
    for sid in student_ids:
        if random.random() > 0.6: # 40% have a hold
            num_holds = np.random.randint(1, 3)
            for _ in range(num_holds):
                htype = np.random.choice(hold_types)
                created_date = datetime(2023, 9, 1) + timedelta(days=np.random.randint(0, 60))
                
                # Logic: some holds unresolved
                is_resolved = random.random() > 0.15
                if is_resolved:
                    days_to_resolve = np.random.randint(1, 30)
                    removed_date = created_date + timedelta(days=days_to_resolve)
                    status = 'Resolved'
                else:
                    removed_date = None
                    days_to_resolve = None
                    status = 'Active'
                
                hold_rows.append({
                    'hold_id': hold_id_counter,
                    'student_id': sid,
                    'hold_type': htype,
                    'hold_created_date': created_date.strftime('%Y-%m-%d'),
                    'hold_removed_date': removed_date.strftime('%Y-%m-%d') if removed_date else None,
                    'status': status,
                    'days_to_resolve': days_to_resolve
                })
                hold_id_counter += 1
                
    df = pd.DataFrame(hold_rows)
    df.to_csv(os.path.join(SYNTHETIC_DIR, 'enrollment_holds.csv'), index=False)
    return df

def generate_advising_interventions(student_ids):
    intervention_types = ['At-Risk Outreach', 'Academic Planning', 'Career Counseling', 'Financial Aid Guidance']
    staff = ['Advisor Smith', 'Advisor Jones', 'Advisor Garcia', 'Advisor Chen']
    outcomes = ['Successful', 'Follow-up Needed', 'No Response', 'In Progress']
    
    int_rows = []
    int_id_counter = 2000
    for sid in student_ids:
        if random.random() > 0.7: # 30% get intervention
            num_int = np.random.randint(1, 3)
            for _ in range(num_int):
                itype = np.random.choice(intervention_types)
                idate = datetime(2023, 10, 1) + timedelta(days=np.random.randint(0, 90))
                
                int_rows.append({
                    'intervention_id': int_id_counter,
                    'student_id': sid,
                    'intervention_type': itype,
                    'intervention_date': idate.strftime('%Y-%m-%d'),
                    'staff_assigned': np.random.choice(staff),
                    'outcome': np.random.choice(outcomes)
                })
                int_id_counter += 1
                
    df = pd.DataFrame(int_rows)
    df.to_csv(os.path.join(SYNTHETIC_DIR, 'advising_interventions.csv'), index=False)
    return df

def generate_course_enrollment(student_ids, students_df, intervention_ids_set, holds_df):
    course_levels = ['100', '200', '300', '400']
    enr_rows = []
    enr_id_counter = 3000
    
    # Identify students with delays
    delayed_students = set(holds_df[holds_df['status'] == 'Active']['student_id'].unique())
    
    for _, row in students_df.iterrows():
        sid = row['student_id']
        num_courses = np.random.randint(3, 6)
        
        # Logic: students with unresolved holds might miss enrollment
        if sid in delayed_students and random.random() > 0.4:
            continue 

        for _ in range(num_courses):
            has_int = sid in intervention_ids_set
            
            # Probability of completion is higher if they had an intervention
            completion_prob = 0.9 if has_int else 0.75
            completed = random.random() < completion_prob
            
            if completed:
                grade = np.random.choice(['A', 'B', 'C', 'D'], p=[0.3, 0.3, 0.3, 0.1])
            else:
                grade = np.random.choice(['F', 'W'], p=[0.6, 0.4])
            
            edate = datetime(2024, 1, 15) + timedelta(days=np.random.randint(-15, 5))
            
            enr_rows.append({
                'enrollment_id': enr_id_counter,
                'student_id': sid,
                'course_level': np.random.choice(course_levels),
                'enrolled_flag': 'Yes',
                'enrollment_date': edate.strftime('%Y-%m-%d'),
                'final_grade': grade,
                'completed_flag': 'Yes' if completed else 'No'
            })
            enr_id_counter += 1
            
    df = pd.DataFrame(enr_rows)
    df.to_csv(os.path.join(SYNTHETIC_DIR, 'course_enrollment.csv'), index=False)
    return df

def mock_uci_dataset():
    # Creating a minimal mock of the UCI dataset to allow scripts to run
    # Columns based on common UCI student success dataset features
    cols = ['Marital status', 'Application mode', 'Application order', 'Course',
            'Daytime/evening attendance', 'Previous qualification', 'Nacionality',
            'Mother\'s qualification', 'Father\'s qualification', 'Mother\'s occupation',
            'Father\'s occupation', 'Displaced', 'Educational special needs', 'Debtor',
            'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment',
            'International', 'Curricular units 1st sem (credited)',
            'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)',
            'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)',
            'Curricular units 1st sem (without evaluations)',
            'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (enrolled)',
            'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)',
            'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)',
            'Unemployment rate', 'Inflation rate', 'GDP', 'Target']
    
    n = 1000
    data = {c: np.random.randint(0, 5, size=n) for c in cols}
    data['Target'] = np.random.choice(['Dropout', 'Enrolled', 'Graduate'], size=n)
    data['Age at enrollment'] = np.random.randint(18, 50, size=n)
    
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(RAW_DIR, 'student_success_uci.csv'), index=False)
    print("Mock UCI dataset created at data/raw/student_success_uci.csv")

if __name__ == "__main__":
    print("Generating synthetic university data...")
    ids, s_df = generate_students(3000)
    p_df = generate_placement_tests(ids)
    h_df = generate_enrollment_holds(ids)
    i_df = generate_advising_interventions(ids)
    
    intervention_ids_set = set(i_df['student_id'].unique())
    generate_course_enrollment(ids, s_df, intervention_ids_set, h_df)
    
    mock_uci_dataset()
    print("All synthetic datasets generated successfully!")
