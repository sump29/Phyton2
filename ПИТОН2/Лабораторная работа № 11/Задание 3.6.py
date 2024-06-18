# Исходный список целых чисел
numbers = [3, -5, 2, 7, -9, 8, 4, -6, 1, -10]

# Разделение списка на положительные и отрицательные числа
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

# Объединение положительных и отрицательных чисел
numbers = positive_numbers + negative_numbers

print(numbers)
