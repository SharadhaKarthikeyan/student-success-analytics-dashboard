# Dashboard Design Plan: Student Success Analytics

This plan outlines a 4-page interactive dashboard designed for University Administrators and Student Success Teams.

## Dashboard Overview
- **Primary Data Source:** `student_success_dashboard_clean.csv`
- **Theme:** Professional Academy (Deep Navy, Slate Gray, Accents of Alert Orange)

---

## Page 1: Executive Overview
**Objective:** Monitor overall health of the student population and identify urgent trends.

### KPIs (Top Ribbon)
- **Total Students:** Count of unique student IDs.
- **Dropout Rate:** % of students with status 'Dropout'.
- **Graduation Rate:** % of students with status 'Graduate'.
- **Enrolled Rate:** % of students with status 'Enrolled'.
- **High-Risk Students:** Count of students in 'High Risk' category.
- **Average Placement Score:** Mean of latest placement scores.
- **Course Completion Rate:** % of courses completed successfully.
- **Avg Hold Resolution Days:** Mean time to clear enrollment holds.

### Visuals
1. **Student Status Distribution:** Donut chart showing Dropout vs. Enrolled vs. Graduate.
2. **Risk Category Distribution:** Stacked bar chart showing % of Low, Medium, High Risk.
3. **Dropout Rate by Major:** Horizontal bar chart sorted by highest rate.
4. **Graduation Rate by GPA Band:** Column chart showing trend from Low to High GPA.

---

## Page 2: Student Risk Analysis
**Objective:** Deep dive into specific demographics and risk factors.

### Visuals
1. **High-Risk Students by Major:** Tree map where box size = student count.
2. **Risk Category by Class Level:** 100% stacked bar chart (Freshman -> Senior).
3. **At-Risk Score Distribution:** Histogram of scores (0-7).
4. **Dropout Rate by First-Generation Status:** Clustered bar chart (First-Gen vs. Not).
5. **Dropout Rate by International Student Status:** Clustered bar chart.

---

## Page 3: Placement Testing Analytics
**Objective:** Evaluate early academic readiness and testing efficiency.

### Visuals
1. **Avg Placement Score by Language:** Bar chart comparing English, Math, etc.
2. **Retake Rate by Language:** Line chart showing % requiring more than 1 attempt.
3. **Placement Score Band Distribution:** Funnel chart (Low, Medium, High).
4. **Total Test Attempts Distribution:** Pie chart (1, 2, 3+ attempts).
5. **Placement Pass/Retake Summary:** Matrix table showing scores vs. attempts.

---

## Page 4: Enrollment Holds and Interventions
**Objective:** Optimize operational support and measure intervention impact.

### Visuals
1. **Hold Resolution Category Distribution:** Stacked bar (Quick, Moderate, Slow).
2. **Average Days to Resolve Holds:** Gauge chart against a 7-day target.
3. **Enrollment Rate by Hold Status:** Side-by-side comparison (Had Hold vs. No Hold).
4. **Course Completion Rate by Intervention Received:** Clustered column chart.
5. **Completion Rate by Intervention Type:** Bar chart sorted by effectiveness.

---

## Recommended Slicers (Sync across all pages)
- **Admission Term** (Multiple Select)
- **Major** (Dropdown)
- **Class Level** (List)
- **Gender** (Buttons)
- **International Student** (Toggle)
- **First-Generation Status** (Toggle)
- **Risk Category** (List)
- **Placement Language** (Dropdown)
