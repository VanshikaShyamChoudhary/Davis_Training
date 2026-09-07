"""
generate_data.py
-----------------
Creates a synthetic but realistic student performance dataset,
inspired by the structure of common "Students Performance" datasets,
with built-in realistic relationships:
- study hours and attendance positively affect scores
- test preparation course completion boosts scores
- parental education level has a mild positive effect
- some random noise so it isn't a perfectly clean signal

Output: data/student_performance.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(7)

N_STUDENTS = 1000

genders = rng.choice(["male", "female"], size=N_STUDENTS)
parental_education = rng.choice(
    ["some high school", "high school", "some college", "associate's degree",
     "bachelor's degree", "master's degree"],
    size=N_STUDENTS,
    p=[0.15, 0.22, 0.22, 0.20, 0.14, 0.07],
)
lunch = rng.choice(["standard", "free/reduced"], size=N_STUDENTS, p=[0.65, 0.35])
test_prep = rng.choice(["none", "completed"], size=N_STUDENTS, p=[0.64, 0.36])

study_hours = np.clip(rng.normal(10, 4, N_STUDENTS), 0, 30)
attendance = np.clip(rng.normal(85, 10, N_STUDENTS), 40, 100)

edu_score_map = {
    "some high school": 0, "high school": 2, "some college": 4,
    "associate's degree": 6, "bachelor's degree": 8, "master's degree": 10,
}
edu_effect = np.array([edu_score_map[e] for e in parental_education])
prep_effect = np.where(test_prep == "completed", 8, 0)
lunch_effect = np.where(lunch == "standard", 4, 0)

base = 45
noise = rng.normal(0, 8, N_STUDENTS)

math_score = (
    base + 1.1 * study_hours + 0.15 * attendance + 0.6 * edu_effect
    + prep_effect + lunch_effect + noise
)
reading_score = (
    base + 0.6 * study_hours + 0.22 * attendance + 0.7 * edu_effect
    + prep_effect * 0.9 + lunch_effect * 0.8 + rng.normal(0, 8, N_STUDENTS)
    + np.where(genders == "female", 3, 0)
)
writing_score = (
    base + 0.55 * study_hours + 0.2 * attendance + 0.75 * edu_effect
    + prep_effect * 1.1 + lunch_effect * 0.8 + rng.normal(0, 8, N_STUDENTS)
    + np.where(genders == "female", 4, 0)
)

df = pd.DataFrame({
    "student_id": np.arange(1, N_STUDENTS + 1),
    "gender": genders,
    "parental_education": parental_education,
    "lunch": lunch,
    "test_prep_course": test_prep,
    "weekly_study_hours": study_hours.round(1),
    "attendance_percent": attendance.round(1),
    "math_score": np.clip(math_score, 0, 100).round(1),
    "reading_score": np.clip(reading_score, 0, 100).round(1),
    "writing_score": np.clip(writing_score, 0, 100).round(1),
})

df["average_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1).round(1)

out_dir = Path(__file__).resolve().parent.parent / "data"
out_dir.mkdir(exist_ok=True)
df.to_csv(out_dir / "student_performance.csv", index=False)

print(f"Generated {len(df)} student records -> data/student_performance.csv")
print(df.head())
