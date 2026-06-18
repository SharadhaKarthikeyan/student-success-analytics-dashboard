# Tableau Build Tutorial

Follow these steps to build the Student Success Dashboard in Tableau.

## 1. Data Connection
1. Open **Tableau Desktop** or **Public**.
2. Click **Connect** -> **To a File** -> **Text File**.
3. Select `student_success_dashboard_clean.csv`.
4. Drag the sheet into the canvas and verify columns.

## 2. Calculated Fields & Logic
1. Right-click in the Data pane and select **Create Calculated Field**.
2. Use the formulas provided in `calculated_fields.md`.
3. Ensure `student_id` is a **Dimension** (not a measure).
4. Set default sort for `Risk Category`: Manual sort as Low, Medium, High.

## 3. Creating Worksheets
**Example: Dropout Rate by Major**
- Drag `Major` to Rows.
- Drag `Dropout Rate` (Calculated Measure) to Columns.
- Sort Descending.
- Color by `Dropout Rate`.

**Example: Status Distribution**
- Change mark type to **Pie**.
- Drag `Student Status` to Color and Label.
- Drag `Student Id` (Count) to Angle and Size.

## 4. Dashboard Assembly
1. Click **New Dashboard**.
2. Set size to **Generic Desktop** (1000 x 800).
3. Use **Vertical and Horizontal Containers** to layout the sections.
4. Drag worksheets onto the canvas.
5. Add **Filters** and set them to "Apply to all using this data source".

## 5. Styling
- **Typeface**: Use 'Open Sans' or 'Segoe UI' for a clean look.
- **Borders**: Add subtle grey borders to containers.
- **Tooltips**: Customize tooltips to explain *why* a student might be at risk.

## 6. Publish
- Go to **Server** -> **Tableau Public** -> **Save to Tableau Public**.
- Copy the embed link for your portfolio website.
