import sys

Z = [5, -3, 2, 0, -7, 1, 8, -4, 6, -1, 3, -5, 4, -2, 7, 9, -6, -8, -9, 10]

min_pos = sys.maxsize

for num in Z:
    if num > 0 and num < min_pos:
        min_pos = num

if min_pos == sys.maxsize:
    print("В списке нет положительных элементов")
else:
    print(f"Наименьший из положительных элементов в списке Z: {min_pos}")