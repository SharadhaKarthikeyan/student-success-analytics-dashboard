-- Analysis Queries for Student Success Analytics

-- 1. Total Students
SELECT COUNT(*) as total_students FROM students;

-- 2. Student Outcome Distribution
SELECT student_status, COUNT(*) as count, 
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM students), 2) as percentage
FROM students
GROUP BY student_status;

-- 3. Dropout Rate by Major
SELECT major, 
       COUNT(*) as total_students,
       SUM(CASE WHEN student_status = 'Dropout' THEN 1 ELSE 0 END) as dropouts,
       ROUND(SUM(CASE WHEN student_status = 'Dropout' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as dropout_rate
FROM students
GROUP BY major
ORDER BY dropout_rate DESC;

-- 4. Dropout Rate by Class Level
SELECT class_level, 
       COUNT(*) as total_students,
       SUM(CASE WHEN student_status = 'Dropout' THEN 1 ELSE 0 END) as dropouts,
       ROUND(SUM(CASE WHEN student_status = 'Dropout' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as dropout_rate
FROM students
GROUP BY class_level;

-- 5. Graduation Rate by GPA Band
SELECT gpa_band, 
       COUNT(*) as total_students,
       SUM(CASE WHEN student_status = 'Graduate' THEN 1 ELSE 0 END) as graduates,
       ROUND(SUM(CASE WHEN student_status = 'Graduate' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as graduation_rate
FROM students
GROUP BY gpa_band;

-- 6. Placement Test Pass Rate by Language
SELECT language, 
       COUNT(*) as total_tests,
       SUM(CASE WHEN passed_flag = 'Yes' THEN 1 ELSE 0 END) as passes,
       ROUND(SUM(CASE WHEN passed_flag = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as pass_rate
FROM placement_tests
GROUP BY language;

-- 7. Retake Rate by Language
SELECT language, 
       COUNT(DISTINCT student_id) as total_students,
       SUM(CASE WHEN attempt_number > 1 THEN 1 ELSE 0 END) as retakes,
       ROUND(SUM(CASE WHEN attempt_number > 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(DISTINCT student_id), 2) as retake_rate
FROM placement_tests
GROUP BY language;

-- 8. Average Placement Score by Attempt Number
SELECT attempt_number, AVG(score) as average_score
FROM placement_tests
GROUP BY attempt_number;

-- 9. Average Days to Resolve Holds by Hold Type
SELECT hold_type, AVG(days_to_resolve) as avg_resolution_days
FROM enrollment_holds
WHERE status = 'Resolved'
GROUP BY hold_type;

-- 10. Unresolved Holds by Hold Type
SELECT hold_type, COUNT(*) as unresolved_count
FROM enrollment_holds
WHERE status = 'Active'
GROUP BY hold_type;

-- 11. Enrollment Rate by Hold Status
WITH hold_status AS (
    SELECT s.student_id, 
           CASE WHEN h.student_id IS NOT NULL THEN 'Had Hold' ELSE 'No Hold' END as hold_group
    FROM students s
    LEFT JOIN enrollment_holds h ON s.student_id = h.student_id
)
SELECT hs.hold_group, 
       COUNT(DISTINCT hs.student_id) as total_students,
       SUM(CASE WHEN ce.enrolled_flag = 'Yes' THEN 1 ELSE 0 END) as enrolled_count,
       ROUND(SUM(CASE WHEN ce.enrolled_flag = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(hs.student_id), 2) as enrollment_rate
FROM hold_status hs
LEFT JOIN course_enrollment ce ON hs.student_id = ce.student_id
GROUP BY hs.hold_group;

-- 12. Course Completion Rate by Intervention Type
SELECT i.intervention_type, 
       COUNT(ce.enrollment_id) as total_enrollments,
       SUM(CASE WHEN ce.completed_flag = 'Yes' THEN 1 ELSE 0 END) as completions,
       ROUND(SUM(CASE WHEN ce.completed_flag = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(ce.enrollment_id), 2) as completion_rate
FROM advising_interventions i
JOIN course_enrollment ce ON i.student_id = ce.student_id
GROUP BY i.intervention_type;

-- 13. Students with High Risk Indicators (Top 10 most recent)
-- Placeholder for complex logic usually calculated in Python or Dashboard
SELECT s.student_id, s.major, s.gpa_band,
       (CASE WHEN s.gpa_band = 'Low' THEN 1 ELSE 0 END + 
        CASE WHEN h.status = 'Active' THEN 1 ELSE 0 END) as simple_risk_score
FROM students s
LEFT JOIN enrollment_holds h ON s.student_id = h.student_id
ORDER BY simple_risk_score DESC
LIMIT 10;

-- 14. Top 10 Majors with Highest Dropout Risk
SELECT major, 
       ROUND(SUM(CASE WHEN student_status = 'Dropout' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as dropout_rate
FROM students
GROUP BY major
ORDER BY dropout_rate DESC
LIMIT 10;

-- 15. Monthly Placement Test Volume
SELECT strftime('%Y-%m', test_date) as month, COUNT(*) as test_volume
FROM placement_tests
GROUP BY month
ORDER BY month;

-- 16. Monthly Hold Creation Trend
SELECT strftime('%Y-%m', hold_created_date) as month, COUNT(*) as holds_created
FROM enrollment_holds
GROUP BY month
ORDER BY month;

-- 17. Advising Intervention Effectiveness (Outcome Distribution)
SELECT outcome, COUNT(*) as count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM advising_interventions), 2) as percentage
FROM advising_interventions
GROUP BY outcome;

-- 18. At-Risk Student Summary for Dashboard
-- Combining factors into a summary view
CREATE VIEW IF NOT EXISTS at_risk_summary AS
SELECT s.student_id, s.major, s.student_status,
       COUNT(DISTINCT h.hold_id) as hold_count,
       MAX(p.score) as max_placement_score,
       COUNT(DISTINCT i.intervention_id) as intervention_count
FROM students s
LEFT JOIN enrollment_holds h ON s.student_id = h.student_id
LEFT JOIN placement_tests p ON s.student_id = p.student_id
LEFT JOIN advising_interventions i ON s.student_id = i.student_id
GROUP BY s.student_id;
