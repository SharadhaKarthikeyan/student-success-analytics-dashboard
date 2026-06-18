# Dashboard KPI Definitions

| KPI Name | Business Meaning | Formula | Required Columns | Chart Type |
| :--- | :--- | :--- | :--- | :--- |
| **Total Students** | Size of the analyzed student cohort. | `COUNT(student_id)` | `student_id` | Big Number Card |
| **Dropout Rate** | Intensity of student attrition. | `Dropouts / Total Students` | `student_status` | Gauge / Card |
| **Graduation Rate** | Primary success metric for the institution. | `Graduates / Total Students` | `student_status` | Gauge / Card |
| **Enrolled Rate** | Percentage of students currently on track. | `Enrolled / Total Students` | `student_status` | Card |
| **High-Risk Count** | Magnitude of the at-risk population. | `COUNT(High Risk Category)`| `risk_category` | Red Alert Card |
| **High-Risk %** | Relative density of potential dropouts. | `High Risk Count / Total Students` | `risk_category` | Card |
| **Avg Placement Score**| Indicator of initial academic readiness. | `AVERAGE(latest_score)` | `latest_placement_score` | Card |
| **Retake Rate** | Efficiency of placement testing. | `% Students with attempts > 1` | `total_test_attempts` | Card / Sparkline |
| **Course Completion Rate** | Academic performance reliability. | `Completions / Total Enrollments`| `completed_flag` | Donut / Card |
| **Avg Hold Resolution** | Speed of administrative support. | `AVERAGE(days_to_resolve)` | `avg_days_to_resolve_hold`| Card (Target < 7) |
| **Unresolved Hold Rate**| Current administrative backlog. | `% with unresolved_hold = Yes` | `unresolved_hold_flag` | Card |
| **Enrollment Delay Rate**| Impact of friction on registration. | `% with delay_flag = Yes` | `enrollment_delay_flag` | Card |
| **Intervention Coverage**| Advisor outreach penetration. | `% with intervention_received = Yes`| `intervention_received_flag`| Card |
