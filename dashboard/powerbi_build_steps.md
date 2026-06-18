# Power BI Build Tutorial

Follow these steps to transform the project CSV into a professional interactive dashboard.

## 1. Import Data
1. Open **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Select `student_success_dashboard_clean.csv`.
4. Click **Transform Data** (Power Query).

## 2. Power Query Fixes
1. Check **Data Types**: 
   - `student_id`: Whole Number.
   - `latest_placement_score`: Decimal Number.
   - `risk_category`: Text.
2. **Sort by Column**:
   - In the "Data View", select `risk_category`. 
   - Select `at_risk_score` (if present) as the "Sort by Column" to ensure Low -> Medium -> High order in charts.
3. Click **Close & Apply**.

## 3. Create Measures
Use the `calculated_fields.md` file to create **New Measures** for:
- `Total Students`, `Dropout Rate`, `Graduation Rate`, and `High Risk %`.

## 4. Build Page 1: Executive Overview
1. **Logo & Title**: Add a text box for the project title.
2. **KPI Ribbon**: Use the **Multi-row card** or individual **Card** visuals for the 8 KPIs.
3. **Status Breakdown**: Use a **Donut Chart** (`student_status` as Legend, `student_id` as Values).
4. **Major Risk**: Use a **Clustered Bar Chart** (`major` as Y-axis, `Dropout Rate` as X-axis).

## 5. Professional Formatting Tips
- **Color Palette**: Go to **View** -> **Themes** -> **Dark Mode** (or customize with deep blues).
- **Backgrounds**: Add a light grey background to the page to make the white visual containers pop.
- **Interactivity**: Select a visual, go to **Format** -> **Edit Interactions** to ensure slicers affect all charts.
- **Sync Slicers**: Ensure the Major and Term slicers are synced across all 4 pages.

## 6. Export for Portfolio
- **Screenshot**: Save high-res screenshots of each page for your GitHub README.
- **Publish**: Click **Publish** to send it to Power BI Service and generate a "Public Link" if you have a Pro license.
