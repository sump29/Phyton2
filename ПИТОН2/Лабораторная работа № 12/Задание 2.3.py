def sum_positive_elements(matrix):
    n = len(matrix)
    sum_positive = 0
    for i in range(n):
        for j in range(n):
            if i >= j and matrix[i][j] > 0:
                sum_positive += matrix[i][j]
    return sum_positive

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

result = sum_positive_elements(matrix)
print(f"Сумма положительных элементов под главной диагональю и на ней: {result}")