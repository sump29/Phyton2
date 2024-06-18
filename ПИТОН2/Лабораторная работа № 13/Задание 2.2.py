def max_letter_frequency(input_str):
    input_str = input_str.lower()
    letter_count = {}
    max_count = 0

    for char in input_str:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
            max_count = max(max_count, letter_count[char])

    return max_count


input_str = input("Введите строку: ")

result = max_letter_frequency(input_str)
print(result)