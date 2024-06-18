num_specialties = int(input("Введите количество специальностей: "))


specialty_dict = {}


for _ in range(num_specialties):
    specialty, group_numbers = input().split(" - ")
    group_numbers = group_numbers.split(", ")
    for group_number in group_numbers:
        specialty_dict[group_number.strip()] = specialty


query_group = input("Введите номер группы для поиска названия специальности: ")


if query_group in specialty_dict:
    specialty = specialty_dict[query_group]
    print(specialty)
else:
    print()