numbers = [int(x) for x in input("Введите числа списка через пробел: ").split()]

divisible_by_6 = [num for num in numbers if num >= 100 and num <= 999 and num % 2 == 0 and num % 6 == 0]

print("Трехзначные четные числа, делимые на 6:", divisible_by_6)