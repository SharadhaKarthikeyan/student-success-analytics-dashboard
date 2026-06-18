# Data Directory

This directory contains the datasets used in the Student Success Analytics Dashboard project.

## Directory Structure

- `raw/`: Contains the original, unmodified datasets.
- `processed/`: Contains datasets that have been cleaned and transformed for analysis and dashboarding.
- `synthetic/`: Contains programmatically generated datasets used to simulate university workflows.

## Dataset Descriptions

### Public Datasets
- **`raw/student_success_uci.csv`**: This is a public dataset sourced from the UCI Machine Learning Repository (Predict Students' Dropout and Academic Success). It contains demographics and academic performance data for a cohort of students.

### Synthetic Datasets
The following datasets were programmatically generated to simulate university administrative data and provide a more comprehensive view of student success factors:
- **`synthetic/students.csv`**: General student demographic and enrollment information.
- **`synthetic/course_enrollment.csv`**: Student course registration and grades.
- **`synthetic/enrollment_holds.csv`**: Tracked holds (e.g., financial, academic) that prevent registration.
- **`synthetic/placement_tests.csv`**: Results of initial placement exams in Math, English, and Science.
- **`synthetic/advising_interventions.csv`**: Records of student interactions with academic advisors.

### Processed Datasets
- **`processed/student_success_clean.csv`**: Cleaned version of the UCI dataset.
- **`processed/student_risk_analysis.csv`**: Merged and feature-engineered dataset combining UCI and synthetic data for risk modeling.

## Important Note on Privacy
**No real student records are used in this project.** All data is either from a publicly available research dataset (UCI) or programmatically generated (synthetic) to ensure student privacy while maintaining realistic data structures for analysis.
