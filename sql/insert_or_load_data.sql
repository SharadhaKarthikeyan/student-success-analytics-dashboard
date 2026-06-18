-- Instructions for loading data from CSVs into the tables.
-- If using SQLite, you can use the following commands in the sqlite3 CLI:

/*
.mode csv
.import data/synthetic/students.csv students
.import data/synthetic/placement_tests.csv placement_tests
.import data/synthetic/enrollment_holds.csv enrollment_holds
.import data/synthetic/advising_interventions.csv advising_interventions
.import data/synthetic/course_enrollment.csv course_enrollment
*/

-- Alternatively, use the provided src/load_to_sqlite.py script to automate this.

-- Manual Insertion Examples for verification:
-- INSERT INTO students VALUES (1, 20, 'Female', 'Computer Science', 'Freshman', 'No', 'Yes', 'Fall 2023', 'Good Standing', 'High', 'Enrolled');
