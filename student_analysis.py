import pandas as pd
import matplotlib.pyplot as plt

students_stats = pd.read_csv('students.csv')
math_score = students_stats["math_score"]

print(students_stats["age"].mean())


