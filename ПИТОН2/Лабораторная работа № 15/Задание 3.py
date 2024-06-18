def filter_and_sum(numbers, a, b, c):
    """Функция для фильтрации и суммирования элементов списка."""
    filtered = [num for num in numbers if a < num < b and num % c == 0]
    remaining = [num for num in numbers if num not in filtered]
    result = sum(remaining)
    return filtered, result


def main():

    input_numbers = input("Введите список чисел через пробел: ").split()
    numbers = [int(num) for num in input_numbers]


    input_ab = input("Введите числа a и b через пробел: ")
    a, b = map(int, input_ab.split())
    input_c = input("Введите число c: ")
    c = int(input_c)


    filtered, result = filter_and_sum(numbers, a, b, c)


    print("Фильтрованные элементы:", filtered)
    print("Сумма остальных элементов:", result)


if __name__ == "__main__":
    main()