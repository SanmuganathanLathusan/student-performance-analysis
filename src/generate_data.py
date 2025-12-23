import pandas as pd
import random

data = []

for i in range(100):
    study_hours = random.randint(1, 10)
    attendance = random.randint(50, 100)
    sleep_hours = random.randint(4, 9)

    pass_fail = 1 if study_hours >= 5 and attendance >= 75 else 0

    data.append([study_hours, attendance, sleep_hours, pass_fail])

df = pd.DataFrame(data, columns=[
    "Study_Hours", "Attendance", "Sleep_Hours", "Pass"
])

df.to_csv("../data/student_data.csv", index=False)
print("Dataset generated successfully!")
