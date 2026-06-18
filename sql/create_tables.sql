-- Create tables for Student Success Analytics Dashboard

-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    major TEXT,
    class_level TEXT,
    international_student TEXT,
    first_generation TEXT,
    admission_term TEXT,
    academic_standing TEXT,
    gpa_band TEXT,
    student_status TEXT
);

-- 2. Placement Tests Table
CREATE TABLE IF NOT EXISTS placement_tests (
    test_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    language TEXT,
    test_date DATE,
    score INTEGER,
    placement_level TEXT,
    attempt_number INTEGER,
    passed_flag TEXT,
    retake_required TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 3. Enrollment Holds Table
CREATE TABLE IF NOT EXISTS enrollment_holds (
    hold_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    hold_type TEXT,
    hold_created_date DATE,
    hold_removed_date DATE,
    status TEXT,
    days_to_resolve INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 4. Advising Interventions Table
CREATE TABLE IF NOT EXISTS advising_interventions (
    intervention_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    intervention_type TEXT,
    intervention_date DATE,
    staff_assigned TEXT,
    outcome TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 5. Course Enrollment Table
CREATE TABLE IF NOT EXISTS course_enrollment (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_level TEXT,
    enrolled_flag TEXT,
    enrollment_date DATE,
    final_grade TEXT,
    completed_flag TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
