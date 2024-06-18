def longest_word_length(input_string):

    words = input_string.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


input_string = input("Введите строку с словами, разделенными пробелами: ")


result = longest_word_length(input_string)
print(f"Длина самого длинного слова в строке: {result}")