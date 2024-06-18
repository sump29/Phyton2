numbers = [int(x) for x in input("Введите числа списка через пробел: ").split()]

total_sum = 0

for num in numbers:
   if num < 0:
       total_sum += num**3

print("Сумма кубов отрицательных чисел списка:", total_sum)