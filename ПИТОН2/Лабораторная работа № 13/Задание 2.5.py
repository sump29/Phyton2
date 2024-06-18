def sum_of_squares_in_range(numbers, start_index, end_index):
    # Функция возвращает сумму квадратов чисел в заданном диапазоне
    return sum(num ** 2 for num in numbers[start_index:end_index + 1])


numbers = list(map(int, input("Введите набор чисел, разделенных пробелами: ").split()))
start_index, end_index = map(int, input("Введите начальный и конечный индексы (включительно): ").split())


if start_index < len(numbers) and end_index < len(numbers) and start_index <= end_index:

    result = sum_of_squares_in_range(numbers, start_index, end_index)
    print(f"Сумма квадратов чисел от {start_index} до {end_index} включительно: {result}")
else:
    print("Некорректные индексы. Убедитесь, что начальный индекс меньше или равен конечному и оба не выходят за пределы массива.")