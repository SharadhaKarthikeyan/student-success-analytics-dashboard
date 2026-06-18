# Data Directory

This directory contains the datasets used in the Student Success Analytics Dashboard project.

## Directory Structure

- `raw/`: Contains the original, unmodified datasets.
- `processed/`: Contains datasets that have been cleaned and transformed for analysis and dashboarding.
- `synthetic/`: Contains programmatically generated datasets used to simulate university workflows.

## Dataset Descriptions

### Public Datasets
- **`raw/student_success_uci.csv`**: This is a public dataset sourced from the **UCI Machine Learning Repository** (dataset name: **Predict Students’ Dropout and Academic Success**). 
  
  > [!IMPORTANT]
  > Users must manually download this dataset and place it at `data/raw/student_success_uci.csv` before running the pipeline. It is used for academic outcome analysis (demographics and academic performance data).
  
  - **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

### Synthetic Datasets
The following datasets are programmatically generated using `src/generate_synthetic_data.py` to simulate university administrative workflows. They do **not** contain any real student records:
- **`synthetic/students.csv`**: General student demographic and enrollment information.
- **`synthetic/course_enrollment.csv`**: Student course registration and grades.
- **`synthetic/enrollment_holds.csv`**: Tracked holds (e.g., financial, academic) that prevent registration.
- **`synthetic/placement_tests.csv`**: Results of initial placement exams in Math, English, and Science.
- **`synthetic/advising_interventions.csv`**: Records of student interactions with academic advisors.

These synthetic datasets are used for placement testing, enrollment holds, advising interventions, and course enrollment workflow analysis.

### Processed Datasets
- **`processed/student_success_clean.csv`**: Cleaned version of the UCI dataset.
- **`processed/student_risk_analysis.csv`**: Merged and feature-engineered dataset combining cleaned UCI outcomes and synthetic administrative workflow data for risk modeling.

## Important Note on Privacy
**No real student records are used in the synthetic datasets.** All administrative workflow data in this project is programmatically generated to demonstrate student success analytics methodologies while maintaining student privacy. The academic outcome trends are modeled using the public, anonymized UCI research dataset.
