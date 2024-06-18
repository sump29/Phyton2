def sum_negative_elements(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        for j in range(n):
            if i > j and matrix[i][j] < 0:
                total += matrix[i][j]
    return total

def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [-7, 8, 9]
]

print("Исходная матрица:")
print_matrix(matrix)

result = sum_negative_elements(matrix)
print("Сумма отрицательных элементов под дополнительной диагональю:", result)