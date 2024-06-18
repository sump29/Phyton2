product = 1

for i in range(10):
  if i % 2 == 0:
      product *= i**2

print("Произведение квадратов однозначных чисел, делящихся на 2:", product)