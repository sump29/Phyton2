def count_spaces_and_check_evenness(text):

    num_spaces = text.count(' ')
    if num_spaces % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")


def main():

    input_text = input("Введите строку: ")


    count_spaces_and_check_evenness(input_text)


if __name__ == "__main__":
    main()