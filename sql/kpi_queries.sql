-- Key Performance Indicators (KPIs) SQL Queries

-- KPI: Overall Dropout Rate
SELECT ROUND(SUM(CASE WHEN student_status = 'Dropout' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as kpi_dropout_rate
FROM students;

-- KPI: Overall Graduation Rate
SELECT ROUND(SUM(CASE WHEN student_status = 'Graduate' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as kpi_graduation_rate
FROM students;

-- KPI: Average Hold Resolution Time (Days)
SELECT ROUND(AVG(days_to_resolve), 1) as kpi_avg_hold_resolution_days
FROM enrollment_holds
WHERE status = 'Resolved';

-- KPI: Overall Placement Test Pass Rate
SELECT ROUND(SUM(CASE WHEN passed_flag = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as kpi_test_pass_rate
FROM placement_tests;

-- KPI: Average GPA (Mocked conversion for analysis)
SELECT ROUND(AVG(CASE WHEN gpa_band = 'High' THEN 3.8 WHEN gpa_band = 'Medium' THEN 3.0 ELSE 2.0 END), 2) as kpi_est_avg_gpa
FROM students;

-- KPI: Percentage of Students with Interventions
SELECT ROUND(COUNT(DISTINCT student_id) * 100.0 / (SELECT COUNT(*) FROM students), 2) as kpi_intervention_reach
FROM advising_interventions;
