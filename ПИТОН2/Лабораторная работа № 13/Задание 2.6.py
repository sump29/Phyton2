def shortest_word_length(words):

    if not words:
        return 0
    min_length = len(words[0])
    for word in words[1:]:
        if len(word) < min_length:
            min_length = len(word)
    return min_length


input_string = input("Введите строку с словами, разделенными пробелами: ")


words = input_string.split()


result = shortest_word_length(words)
print(f"Длина самого короткого слова в строке: {result}")