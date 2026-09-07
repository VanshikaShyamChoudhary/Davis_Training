"""
sql_queries.py
----------------
Runs a set of SQL queries directly against the SQLite database to
answer common analytical questions. Results are printed and also
saved as CSVs for use in the report / visualizations.
"""

import sqlite3
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parent.parent
conn = sqlite3.connect(root / "data" / "student_performance.db")
out_dir = root / "sql"
out_dir.mkdir(exist_ok=True)

queries = {
    "avg_scores_by_gender": """
        SELECT gender,
               ROUND(AVG(math_score), 2) AS avg_math,
               ROUND(AVG(reading_score), 2) AS avg_reading,
               ROUND(AVG(writing_score), 2) AS avg_writing,
               ROUND(AVG(average_score), 2) AS avg_overall,
               COUNT(*) AS num_students
        FROM students
        GROUP BY gender;
    """,
    "avg_scores_by_parental_education": """
        SELECT parental_education,
               ROUND(AVG(average_score), 2) AS avg_overall,
               COUNT(*) AS num_students
        FROM students
        GROUP BY parental_education
        ORDER BY avg_overall DESC;
    """,
    "test_prep_effect": """
        SELECT test_prep_course,
               ROUND(AVG(math_score), 2) AS avg_math,
               ROUND(AVG(reading_score), 2) AS avg_reading,
               ROUND(AVG(writing_score), 2) AS avg_writing,
               COUNT(*) AS num_students
        FROM students
        GROUP BY test_prep_course;
    """,
    "lunch_type_effect": """
        SELECT lunch,
               ROUND(AVG(average_score), 2) AS avg_overall,
               COUNT(*) AS num_students
        FROM students
        GROUP BY lunch;
    """,
    "top_10_performers": """
        SELECT student_id, gender, parental_education, test_prep_course, average_score
        FROM students
        ORDER BY average_score DESC
        LIMIT 10;
    """,
    "pass_fail_summary": """
        SELECT
            CASE WHEN average_score >= 70 THEN 'Pass' ELSE 'Fail' END AS result,
            COUNT(*) AS num_students,
            ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM students), 2) AS percentage
        FROM students
        GROUP BY result;
    """,
    "study_hours_buckets": """
        SELECT
            CASE
                WHEN weekly_study_hours < 5 THEN '0-5 hrs'
                WHEN weekly_study_hours < 10 THEN '5-10 hrs'
                WHEN weekly_study_hours < 15 THEN '10-15 hrs'
                WHEN weekly_study_hours < 20 THEN '15-20 hrs'
                ELSE '20+ hrs'
            END AS study_bucket,
            ROUND(AVG(average_score), 2) AS avg_overall,
            COUNT(*) AS num_students
        FROM students
        GROUP BY study_bucket
        ORDER BY MIN(weekly_study_hours);
    """,
}

for name, sql in queries.items():
    result = pd.read_sql_query(sql, conn)
    print(f"\n--- {name} ---")
    print(result.to_string(index=False))
    result.to_csv(out_dir / f"{name}.csv", index=False)

conn.close()
print(f"\nSaved {len(queries)} query results to sql/")
