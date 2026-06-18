# Calculated Fields: Power BI (DAX) & Tableau

This document provides the specific formulas needed to build the analysis logic within your BI tool.

## 1. General Metrics
| Metric | Power BI (DAX) | Tableau (Calculated Field) |
| :--- | :--- | :--- |
| **Total Students** | `Total Students = COUNTROWS('Table')` | `COUNTD([Student Id])` |
| **Dropout Count** | `Dropouts = CALCULATE(COUNT('Table'[student_id]), 'Table'[student_status] = "Dropout")` | `IF [Student Status] = "Dropout" THEN 1 END` |
| **Dropout Rate** | `Dropout Rate = DIVIDE([Dropouts], [Total Students], 0)` | `SUM([Dropout Count]) / [Total Students]` |
| **Graduate Count** | `Graduates = CALCULATE(COUNT('Table'[student_id]), 'Table'[student_status] = "Graduate")` | `IF [Student Status] = "Graduate" THEN 1 END` |
| **Graduation Rate** | `Grad Rate = DIVIDE([Graduates], [Total Students], 0)` | `SUM([Graduate Count]) / [Total Students]` |

## 2. Risk Metrics
| Metric | Power BI (DAX) | Tableau (Calculated Field) |
| :--- | :--- | :--- |
| **High Risk Students** | `High Risk Students = CALCULATE(COUNT('Table'[student_id]), 'Table'[risk_category] = "High Risk")` | `IF [Risk Category] = "High Risk" THEN 1 END` |
| **High Risk %** | `High Risk % = DIVIDE([High Risk Students], [Total Students], 0)` | `SUM([High Risk Students]) / [Total Students]` |

## 3. Academic & Operational Metrics
| Metric | Power BI (DAX) | Tableau (Calculated Field) |
| :--- | :--- | : :--- |
| **Retake Rate** | `Retake Rate = DIVIDE(CALCULATE(COUNT('Table'[student_id]), 'Table'[total_test_attempts] > 1), [Total Students])` | `COUNTD(IF [Total Test Attempts] > 1 THEN [Student Id] END) / [Total Students]` |
| **Course Comp. Rate** | `Completion Rate = DIVIDE(CALCULATE(COUNT('Table'[student_id]), 'Table'[completed_flag] = "Yes"), [Total Students])` | `SUM(IF [Completed Flag] = "Yes" THEN 1 ELSE 0 END) / COUNT([Student Id])` |
| **Unresolved Hold Rate**| `Unres Hold % = DIVIDE(CALCULATE(COUNT('Table'[student_id]), 'Table'[unresolved_hold_flag] = "Yes"), [Total Students])` | `SUM(IF [Unresolved Hold Flag] = "Yes" THEN 1 ELSE 0 END) / [Total Students]` |
| **Enroll Delay Rate** | `Delay Rate = DIVIDE(CALCULATE(COUNT('Table'[student_id]), 'Table'[enrollment_delay_flag] = "Yes"), [Total Students])` | `SUM(IF [Enrollment Delay Flag] = "Yes" THEN 1 ELSE 0 END) / [Total Students]` |
| **Intervention Rate** | `Intervention Rate = DIVIDE(CALCULATE(COUNT('Table'[student_id]), 'Table'[intervention_received_flag] = "Yes"), [Total Students])` | `SUM(IF [Intervention Received Flag] = "Yes" THEN 1 ELSE 0 END) / [Total Students]` |
