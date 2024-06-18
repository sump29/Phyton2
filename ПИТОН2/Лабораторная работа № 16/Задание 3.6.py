numbers = [int(x) for x in input("Введите числа списка через пробел: ").split()]

divisible_by_11 = [num for num in numbers if num % 2 != 0 and num % 11 == 0]

print("Нечетные числа, делимые на 11:", divisible_by_11)