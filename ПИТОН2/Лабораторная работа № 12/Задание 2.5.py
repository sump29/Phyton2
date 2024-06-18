def sum_above_extra_diagonal(matrix):
    n = len(matrix)
    total_sum = 0
    for i in range(n):
        for j in range(n):
            if i < n - j - 1 and matrix[i][j] > 0:
                total_sum += matrix[i][j]
    return total_sum

def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [7, 8, -9]
]

extra_diagonal_sum = sum_above_extra_diagonal(matrix)

print("Исходная матрица:")
print_matrix(matrix)
print("Сумма положительных элементов над дополнительной диагональю:", extra_diagonal_sum)