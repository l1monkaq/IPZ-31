class Student:
    def __init__(self, name, group, score):
        self.name, self.group, self.score = name, group, score

    def show_info(self):
        print(f"Студент: {self.name}\nГрупа: {self.group}\nБал: {self.score}\n{'-'*20}")

students = [
    Student("Ничек Станіслав", "ІПЗ-21", 7.5),
    Student("Абдульманов Данило", "ІПЗ-12", 8.6),
    Student("Якимчук Єва", "ІПЗ-23", 6.7)
]

for s in students: s.show_info()