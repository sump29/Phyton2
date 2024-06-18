num_entries = int(input("Введите количество записей в словаре: "))


dictionary = {}


for _ in range(num_entries):
    word, description = input().split(" - ")
    dictionary[word] = description


query_word = input("Введите слово для поиска значения в словаре: ")


if query_word in dictionary:
    description = dictionary[query_word]
    print(description)
else:
    print("Нет в словаре")