"""
analysis.py
-------------
Pandas/NumPy-based analysis: grading, pass/fail, z-scores,
and correlation matrix, saved for use in visualizations and reporting.
"""

import numpy as np
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "data" / "student_performance.csv")


def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


df["grade"] = df["average_score"].apply(assign_grade)
df["result"] = np.where(df["average_score"] >= 70, "Pass", "Fail")

# z-score (NumPy) to flag statistically strong/weak performers
mean_score = df["average_score"].mean()
std_score = df["average_score"].std()
df["z_score"] = ((df["average_score"] - mean_score) / std_score).round(2)
df["performance_flag"] = np.select(
    [df["z_score"] >= 1.5, df["z_score"] <= -1.5],
    ["Top Performer", "Needs Support"],
    default="Average",
)

correlation_cols = ["weekly_study_hours", "attendance_percent", "math_score",
                     "reading_score", "writing_score", "average_score"]
corr_matrix = df[correlation_cols].corr().round(3)

grade_dist = df["grade"].value_counts().sort_index()
flag_dist = df["performance_flag"].value_counts()

out_dir = root / "data"
df.to_csv(out_dir / "student_performance_enriched.csv", index=False)
corr_matrix.to_csv(out_dir / "correlation_matrix.csv")

print("Grade distribution:\n", grade_dist)
print("\nPerformance flag distribution:\n", flag_dist)
print("\nCorrelation matrix:\n", corr_matrix)
print(f"\nOverall pass rate: {(df['result'] == 'Pass').mean() * 100:.1f}%")
print("\nSaved enriched dataset -> data/student_performance_enriched.csv")
