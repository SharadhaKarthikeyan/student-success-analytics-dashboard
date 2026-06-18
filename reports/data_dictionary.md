# Data Dictionary

## Table: students
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| student_id | INTEGER | Unique identifier for each student | 1001 |
| age | INTEGER | Age of student at enrollment | 22 |
| gender | TEXT | Self-identified gender | Female |
| major | TEXT | Degree program enrolled in | Nursing |
| class_level | TEXT | Current academic year | Junior |
| international_student | TEXT | Whether the student is international (Yes/No) | No |
| first_generation | TEXT | Whether student is first-gen (Yes/No) | Yes |
| admission_term | TEXT | Term when student was admitted | Fall 2023 |
| academic_standing | TEXT | Official standing (Good, Probation, Warning) | Good Standing |
| gpa_band | TEXT | Category of GPA (High, Medium, Low) | High |
| student_status | TEXT | Outcome status (Dropout, Enrolled, Graduate) | Enrolled |

## Table: placement_tests
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| test_id | INTEGER | Unique identifier for test attempt | 5001 |
| student_id | INTEGER | ID of the student taking the test | 1001 |
| language | TEXT | Subject of the test (English, Math, etc.) | Math |
| test_date | DATE | Date the test was taken | 2023-08-15 |
| score | INTEGER | Score achieved (0-100) | 78 |
| placement_level| TEXT | Recommended level based on score | Intermediate |
| attempt_number | INTEGER| Chronological attempt number | 1 |
| passed_flag | TEXT | Whether student passed the test | Yes |
| retake_required | TEXT | Flag to indicate another attempt is needed | No |

## Table: enrollment_holds
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| hold_id | INTEGER | Unique identifier for the hold | 8001 |
| student_id | INTEGER | ID of the student with the hold | 1001 |
| hold_type | TEXT | Category (Financial, Advising, etc.) | Financial |
| hold_created_date | DATE | Date the hold was placed | 2023-09-10 |
| hold_removed_date | DATE | Date the hold was cleared | 2023-09-15 |
| status | TEXT | Current state (Active, Resolved) | Resolved |
| days_to_resolve | INTEGER | Days between creation and removal | 5 |

## Table: advising_interventions
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| intervention_id | INTEGER | Unique identifier for the meeting | 2001 |
| student_id | INTEGER | ID of the student | 1001 |
| intervention_type | TEXT | Purpose of the meeting | At-Risk Outreach |
| intervention_date | DATE | Date of the intervention | 2023-11-05 |
| staff_assigned | TEXT | Advisor name | Advisor Jones |
| outcome | TEXT | Result (Successful, Follow-up, etc.) | Successful |

## Table: course_enrollment
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| enrollment_id | INTEGER | Unique identifier for enrollment record | 3001 |
| student_id | INTEGER | ID of the student | 1001 |
| course_level | TEXT | Level (100, 200, 300, 400) | 200 |
| enrolled_flag | TEXT | Whether student enrolled (Yes/No) | Yes |
| enrollment_date | DATE | Date student registered | 2024-01-20 |
| final_grade | TEXT | Grade (A, B, C, D, F, W) | B |
| completed_flag | TEXT | Whether course was finished successfully | Yes |
