def process_student_results(data):
    averages = {k: round(sum(v)/len(v), 2) for k, v in data.items() if v}
    unique_scores = {val for sub in data.values() for val in sub}
    return averages, sorted(unique_scores)

students_data = {
    "Катерина": [88, 92, 85, 90],
    "Максим": [75, 72, 80, 78],
    "Юлія": [95, 98, 92, 94],
    "Артем": [82, 85, 82, 88]
}

avgs, unique_vals = process_student_results(students_data)

print("Середні бали:", avgs)
print("Унікальні оцінки:", unique_vals)
print("Кількість унікальних:", len(unique_vals))