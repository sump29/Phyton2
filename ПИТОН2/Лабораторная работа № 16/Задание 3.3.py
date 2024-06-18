numbers = [int(x) for x in input("Введите числа списка через пробел: ").split()]

for num in numbers:
  if num % 2 == 0:
      print(num, end=" ")