students = [
    {"prizv": "Ничек", "imya": "Станіслав", "grades": [9, 10, 11, 7, 8]},
    {"prizv": "Абдульманов", "imya": "Данило", "grades": [8, 9, 9, 7, 10]},
    {"prizv": "Якимчук", "imya": "Єва", "grades": [10, 10, 11, 10, 11]},
]

num_subs = len(students[0]["grades"])
sub_totals = [0] * num_subs

print("Прізвище    | Ім’я      | Сер. бал")
print("-" * 35)

for s in students:
    avg = sum(s["grades"]) / num_subs
    print(f"{s['prizv']:<11} | {s['imya']:<9} | {avg:.2f}")
    
    for i in range(num_subs):
        sub_totals[i] += s["grades"][i]

print("-" * 35)
group_avg = [round(total / len(students), 1) for total in sub_totals]
print(f"Середнє по предметах: {group_avg}")