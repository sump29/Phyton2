num_employees = int(input("Введите количество сотрудников: "))


vacation_schedule = {}


for _ in range(num_employees):
    surname, day, month = input().split()
    if month not in vacation_schedule:
        vacation_schedule[month] = []
    vacation_schedule[month].append(surname)


query_month = input("Введите название месяца для поиска фамилий сотрудников с отпуском: ")


if query_month in vacation_schedule:
    surnames = vacation_schedule[query_month]
    if surnames:
        print(" ".join(surnames))
    else:
        print()
else:
    print()