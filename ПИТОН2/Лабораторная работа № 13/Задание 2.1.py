def capitalize_words_with_hyphens(input_str):
    words = input_str.split()

    capitalized_words = []
    for word in words:
        capitalized_word = "-".join(c.upper() for c in word)
        capitalized_words.append(capitalized_word)

    result_str = " ".join(capitalized_words)
    return result_str

# Ввод строки с несколькими словами
input_str = input("Введите несколько слов: ")

result = capitalize_words_with_hyphens(input_str)
print(result)
