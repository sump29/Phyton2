def reverse_words_with_plus(input_string):

    words = input_string.split()
    reversed_words = [word[::-1] + '+' * (len(word) - 1) for word in words]
    return ' '.join(reversed_words)


input_string = input("Введите строку с словами: ")


result = reverse_words_with_plus(input_string)
print(f"Строка с перевернутыми словами и плюсами между буквами: {result}")