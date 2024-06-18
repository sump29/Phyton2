total_sum = 0

for i in range(100, 1000):
   if i % 8 == 0:
       total_sum += i**3

print("Сумма кубов всех трехзначных чисел, делящихся на 8:", total_sum)