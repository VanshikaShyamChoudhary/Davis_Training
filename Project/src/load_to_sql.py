"""
load_to_sql.py
----------------
Loads the generated CSV into a SQLite database so the project
can demonstrate real SQL querying, not just pandas.

Output: data/student_performance.db
"""

import sqlite3
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "data" / "student_performance.csv")

db_path = root / "data" / "student_performance.db"
conn = sqlite3.connect(db_path)
df.to_sql("students", conn, if_exists="replace", index=False)

cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM students")
count = cur.fetchone()[0]
print(f"Loaded {count} rows into students table -> data/student_performance.db")

conn.close()
