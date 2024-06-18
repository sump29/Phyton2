def count_upper_and_lower_case_letters(text):

    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


def main():

    input_text = input("Введите строку: ")


    upper_count, lower_count = count_upper_and_lower_case_letters(input_text)

    
    print(f"Количество букв верхнего регистра: {upper_count}")
    print(f"Количество букв нижнего регистра: {lower_count}")


if __name__ == "__main__":
    main()