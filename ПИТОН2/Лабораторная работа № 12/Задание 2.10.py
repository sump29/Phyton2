def find_min_element_position(matrix):
    min_element = matrix[0][0]
    min_row = 0
    min_col = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_row = i
                min_col = j

    return min_row, min_col


def print_matrix(matrix):
    for row in matrix:
        print(row)



matrix = [
    [5, 2, 7],
    [1, 6, 3],
    [9, 4, 8]
]

print("Исходная матрица:")
print_matrix(matrix)

min_row, min_col = find_min_element_position(matrix)
print("\nМинимальный элемент матрицы:", matrix[min_row][min_col])
print("Номер строки минимального элемента:", min_row)
print("Номер столбца минимального элемента:", min_col)