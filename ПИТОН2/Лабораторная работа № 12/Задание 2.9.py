def replace_negatives_with_zeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = [
    [5, -2, 7],
    [1, -6, 3],
    [9, 4, -8]
]

print("Исходная матрица:")
print_matrix(matrix)

processed_matrix = replace_negatives_with_zeros(matrix)

print("\nМатрица после замены отрицательных элементов на нули:")
print_matrix(processed_matrix)