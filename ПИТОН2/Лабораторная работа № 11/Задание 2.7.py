temperatures = [2, -1, -3, 5, -2, 0, -4, -1, 3, 6, -1, -5, 0, 2, -3, -4, 1, -1, 4, 0, -2, -3, -3, -2, 2, -1, -4, -3, 0, 4]
count_below_zero = 0

for temp in temperatures:
    if temp < 0:
        count_below_zero += 1

print(f"Температура опускалась ниже 0° C {count_below_zero} раз в марте.")