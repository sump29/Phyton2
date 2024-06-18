def filter_even_greater_than_10(numbers):

    return [num for num in numbers if num > 10 and num % 2 == 0]


def main():

    input_numbers = input("Введите список чисел через пробел: ").split()
    numbers = [int(num) for num in input_numbers]


    filtered_numbers = filter_even_greater_than_10(numbers)

    
    print("Отфильтрованный список четных чисел больше 10:", filtered_numbers)


if __name__ == "__main__":
    main()