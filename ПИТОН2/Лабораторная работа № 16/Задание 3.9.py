total_sum = 0

for i in range(10, 100):
  if i % 7 == 0:
      total_sum += i**2

print("Сумма квадратов двузначных чисел, делящихся на 7:", total_sum)