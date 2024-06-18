numbers = [int(x) for x in input("Введите числа списка через пробел: ").split()]

divisible_by_17 = [num for num in numbers if num % 17 == 0]

print("Числа, делимые на 17:", divisible_by_17)