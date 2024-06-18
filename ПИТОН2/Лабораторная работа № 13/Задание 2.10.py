def max_char_count(input_string):

    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    max_count = max(char_counts.values())
    return max_count


input_string = input("Введите строку: ")


result = max_char_count(input_string)
print(f"Максимальное количество вхождений символа в строке: {result}")