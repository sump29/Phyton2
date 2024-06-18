num_grades = int(input("Введите количество оценок: "))
grades = []

for i in range(num_grades):
    grade = float(input(f"Введите оценку {i+1}: "))
    grades.append(grade)

print("\nОценки:")
for grade in grades:
    print(grade)

average_grade = sum(grades) / len(grades)
print(f"\nСредняя оценка за урок: {average_grade}")