Y = [7, 10, 5, 3, 9, 12, 1, 15, 6, 8, 2, 11, 4, 14, 13]

min_value = Y[0]
min_index = 0

for i in range(1, len(Y)):
    if Y[i] < min_value:
        min_value = Y[i]
        min_index = i

print("Наименьшее значение в списке Y:", min_value)
print("Порядковый номер наименьшего элемента в списке Y:", min_index)