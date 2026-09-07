# Student Performance Analysis — Data Visualization Project

A complete data analysis and visualization project covering the full stack requested:
**Python, SQL, Pandas, NumPy, Matplotlib, and Seaborn.**

## Project structure

```
student_performance/
├── src/
│   ├── generate_data.py     # creates the synthetic dataset
│   ├── load_to_sql.py       # loads CSV into a SQLite database
│   ├── sql_queries.py       # runs SQL aggregation queries
│   ├── analysis.py          # Pandas/NumPy feature engineering & stats
│   └── visualize.py         # Matplotlib/Seaborn visualizations
├── data/                     # CSVs + SQLite database
├── sql/                      # saved SQL query results (CSVs)
├── plots/                    # 8 PNG charts
└── README.md
```

## The dataset

`generate_data.py` simulates **1,000 students** with realistic relationships between
study habits and academic outcomes — inspired by the structure of common
"Students Performance in Exams" datasets. Fields include:

- Demographics: `gender`, `parental_education`, `lunch` (proxy for socioeconomic status)
- Behavioral: `weekly_study_hours`, `attendance_percent`, `test_prep_course`
- Outcomes: `math_score`, `reading_score`, `writing_score`, `average_score`

Scores are generated so that study hours, attendance, test-prep completion, and
parental education level all have a genuine (but noisy) positive effect —
enough realistic structure for the SQL/Pandas/visualization work to reveal real patterns.

## Pipeline

Run in order from the project root:

```bash
python3 src/generate_data.py     # -> data/student_performance.csv
python3 src/load_to_sql.py       # -> data/student_performance.db
python3 src/sql_queries.py       # -> sql/*.csv (7 query results)
python3 src/analysis.py          # -> data/student_performance_enriched.csv
python3 src/visualize.py         # -> plots/01-08 (8 PNG charts)
```

## SQL component

`sql_queries.py` runs 7 SQL queries directly against the SQLite database using
`GROUP BY`, `CASE WHEN`, aggregate functions, and subqueries:

1. Average scores by gender
2. Average scores by parental education level
3. Effect of test preparation course completion
4. Effect of lunch type (standard vs. free/reduced)
5. Top 10 performing students
6. Pass/fail summary (threshold: average score ≥ 70)
7. Average score by weekly study-hour bucket

## Pandas / NumPy component

`analysis.py` adds:
- **Grade assignment** (A–F) via a custom function applied row-wise
- **Pass/Fail** classification
- **Z-scores** (NumPy) to flag statistically strong/weak performers
- **Performance flags**: Top Performer / Average / Needs Support, via `np.select`
- **Correlation matrix** across study hours, attendance, and all score columns

## Key findings

| Factor | Effect on Average Score |
|---|---|
| Test prep course completed | +8–9 points on average |
| Standard lunch (vs. free/reduced) | +3 points on average |
| Parental education (bachelor's+ vs. some high school) | +5–6 points |
| Weekly study hours | Strong positive correlation (r ≈ 0.41) |
| Attendance % | Moderate positive correlation (r ≈ 0.22) |

Overall pass rate (≥70 average): **85.3%**. Female students scored slightly higher
on average across all three subjects in this dataset.

## Visualizations (Matplotlib + Seaborn)

1. Distribution of average scores (histogram + KDE, pass threshold marked)
2. Average scores by gender and subject (grouped bar chart)
3. Average score by parental education level (horizontal bar chart)
4. Test preparation course vs. average score (boxplot)
5. Weekly study hours vs. average score (scatter + regression line)
6. Attendance % vs. average score (scatter + regression line)
7. Correlation heatmap across all numeric factors
8. Grade distribution (A–F countplot)

## Extending this project

- Swap the synthetic generator for a real school/exam dataset export.
- Add a simple classification model (e.g., logistic regression) to predict Pass/Fail.
- Build an interactive dashboard (Streamlit/Plotly Dash) on top of the same SQL layer.
- Add more SQL joins if extending to a multi-table schema (e.g., separate `students`,
  `subjects`, and `scores` tables instead of one flat table).
