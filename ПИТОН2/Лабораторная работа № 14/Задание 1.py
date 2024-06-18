num_entries = int(input("Введите количество номеров телефонов: "))


phonebook = {}


for _ in range(num_entries):
    name, phone = input().split()
    phonebook[name] = phone


query_name = input("Введите имя для поиска номера телефона: ")


if query_name in phonebook:
    phone = phonebook[query_name]
    print("Номер телефона:", phone)
else:
    print("Нет в телефонной книге")