"""
visualize.py
--------------
Generates 8 visualizations covering distributions, comparisons,
and correlations, using Matplotlib and Seaborn.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="whitegrid")
root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "data" / "student_performance_enriched.csv")
plots_dir = root / "plots"
plots_dir.mkdir(exist_ok=True)

# 1. Distribution of average scores
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["average_score"], bins=25, kde=True, ax=ax, color="#4C72B0")
ax.axvline(70, color="red", linestyle="--", label="Pass threshold (70)")
ax.set_title("Distribution of Average Scores")
ax.set_xlabel("Average Score")
ax.legend()
fig.tight_layout()
fig.savefig(plots_dir / "01_score_distribution.png", dpi=150)
plt.close(fig)

# 2. Average scores by gender
fig, ax = plt.subplots(figsize=(7, 5))
score_cols = ["math_score", "reading_score", "writing_score"]
melted = df.melt(id_vars="gender", value_vars=score_cols, var_name="subject", value_name="score")
sns.barplot(data=melted, x="subject", y="score", hue="gender", ax=ax, palette="Set2")
ax.set_title("Average Scores by Gender and Subject")
ax.set_ylabel("Average Score")
fig.tight_layout()
fig.savefig(plots_dir / "02_scores_by_gender.png", dpi=150)
plt.close(fig)

# 3. Average score by parental education
fig, ax = plt.subplots(figsize=(9, 5))
edu_order = df.groupby("parental_education")["average_score"].mean().sort_values().index
sns.barplot(data=df, y="parental_education", x="average_score", order=edu_order, ax=ax, color="#55A868")
ax.set_title("Average Score by Parental Education Level")
ax.set_xlabel("Average Score")
ax.set_ylabel("")
fig.tight_layout()
fig.savefig(plots_dir / "03_score_by_parental_education.png", dpi=150)
plt.close(fig)

# 4. Test prep course effect (boxplot)
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x="test_prep_course", y="average_score", ax=ax, palette="Set3")
ax.set_title("Test Preparation Course vs. Average Score")
fig.tight_layout()
fig.savefig(plots_dir / "04_test_prep_effect.png", dpi=150)
plt.close(fig)

# 5. Study hours vs average score (scatter with regression line)
fig, ax = plt.subplots(figsize=(7, 5))
sns.regplot(data=df, x="weekly_study_hours", y="average_score", ax=ax,
            scatter_kws={"alpha": 0.3, "s": 20}, line_kws={"color": "red"})
ax.set_title("Weekly Study Hours vs. Average Score")
fig.tight_layout()
fig.savefig(plots_dir / "05_study_hours_vs_score.png", dpi=150)
plt.close(fig)

# 6. Attendance vs average score
fig, ax = plt.subplots(figsize=(7, 5))
sns.regplot(data=df, x="attendance_percent", y="average_score", ax=ax,
            scatter_kws={"alpha": 0.3, "s": 20, "color": "#C44E52"}, line_kws={"color": "darkred"})
ax.set_title("Attendance % vs. Average Score")
fig.tight_layout()
fig.savefig(plots_dir / "06_attendance_vs_score.png", dpi=150)
plt.close(fig)

# 7. Correlation heatmap
corr_cols = ["weekly_study_hours", "attendance_percent", "math_score",
             "reading_score", "writing_score", "average_score"]
corr = df[corr_cols].corr()
fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax, square=True)
ax.set_title("Correlation Heatmap - Study Factors & Scores")
fig.tight_layout()
fig.savefig(plots_dir / "07_correlation_heatmap.png", dpi=150)
plt.close(fig)

# 8. Grade distribution
fig, ax = plt.subplots(figsize=(7, 5))
grade_order = ["A", "B", "C", "D", "F"]
sns.countplot(data=df, x="grade", order=grade_order, ax=ax, palette="viridis")
ax.set_title("Grade Distribution")
ax.set_xlabel("Grade")
ax.set_ylabel("Number of Students")
fig.tight_layout()
fig.savefig(plots_dir / "08_grade_distribution.png", dpi=150)
plt.close(fig)

print("Saved 8 plots to plots/")
