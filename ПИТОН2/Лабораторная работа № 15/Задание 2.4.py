def calculate_sum_and_product(numbers):

    if len(numbers) == 0:
        return 0, 1
    else:
        sum_numbers = sum(numbers)
        product_numbers = 1
        for num in numbers:
            product_numbers *= num
        return sum_numbers, product_numbers


def main():

    input_numbers = input("Введите список чисел через пробел: ").split()
    numbers = [float(num) for num in input_numbers]


    sum_numbers, product_numbers = calculate_sum_and_product(numbers)


    print("Сумма элементов списка:", sum_numbers)
    print("Произведение элементов списка:", product_numbers)


if __name__ == "__main__":
    main()