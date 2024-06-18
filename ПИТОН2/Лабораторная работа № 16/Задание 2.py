def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)

def combination(n, m):
   return factorial(n) / (factorial(m) * factorial(n-m))

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

result = combination(n, m)
print("Значение выражения C =", result)