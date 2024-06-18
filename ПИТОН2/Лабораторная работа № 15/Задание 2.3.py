def calculate_average(numbers):

    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)


def main():

    input_numbers = input("Введите список чисел через пробел: ").split()
    numbers = [int(num) for num in input_numbers]


    average = calculate_average(numbers)


    print("Среднее значение элементов списка:", average)


if __name__ == "__main__":
    main()