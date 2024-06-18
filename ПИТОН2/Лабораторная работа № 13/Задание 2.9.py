def sorted_letters(input_string):

    words = input_string.split()
    letters = sorted(set(''.join(words)))


input_string = input("Введите строку с словами: ")


result = sorted_letters(input_string)
print(f"Буквы введенных слов в алфавитном порядке, разделенные двоеточием: {result}")