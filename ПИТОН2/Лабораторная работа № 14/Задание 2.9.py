def find_birthdays_in_month(num_students, student_data, month):

    birthdays_in_month = []
    for data in student_data:
        name, day, month_name = data.split()
        if month_name == month:
            birthdays_in_month.append((name, day))
    return birthdays_in_month



num_students = int(input("Введите количество одноклассников: "))
student_data = [input(f"Введите имя, день и месяц рождения одноклассника {i + 1} (разделите пробелом): ").strip() for i
                in range(num_students)]
month_query = input("Введите название месяца: ").strip()

birthdays_in_month = find_birthdays_in_month(num_students, student_data, month_query)


for name, day in birthdays_in_month:
    print(f"{name} {day}")