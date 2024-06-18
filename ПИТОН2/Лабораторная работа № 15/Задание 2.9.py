def add_numbers_to_list(numbers_str, numbers_list):

    numbers = [int(num) for num in numbers_str.split(';')]
    numbers_list.extend(numbers)


def main():

    input_str = input("Введите числа через точку с запятой: ")


    input_list = input("Введите список: ").split()
    numbers_list = [int(num) for num in input_list]


    add_numbers_to_list(input_str, numbers_list)


    print("Итоговый список:", numbers_list)


if __name__ == "__main__":
    main()