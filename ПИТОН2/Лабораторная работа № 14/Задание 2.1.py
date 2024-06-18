# Ввод количества студентов
num_students = int(input("Введите количество студентов: "))

# Создание словаря для хранения данных
student_dict = {}

# Ввод данных о студентах
for _ in range(num_students):
    surname, specialty, group = input().split()
    if specialty not in student_dict:
        student_dict[specialty] = []
    student_dict[specialty].append(surname)

# Ввод запроса
query_specialty = input("Введите название специальности для поиска фамилий студентов: ")

# Поиск фамилий студентов по специальности
if query_specialty in student_dict:
    surnames = student_dict[query_specialty]
    if surnames:
        print(", ".join(surnames))
    else:
        print("Проверьте запрос")
else:
    print("Проверьте запрос")