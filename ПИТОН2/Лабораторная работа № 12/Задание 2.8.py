def sort_matrix(matrix):
    n = len(matrix)
    sorted_matrix = [[0]*len(matrix[0]) for _ in range(n)]
    for i in range(n):
        sorted_matrix[i] = sorted(matrix[i])
    return sorted_matrix

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

sorted_matrix = sort_matrix(matrix)

print("\nОтсортированная матрица:")
print_matrix(sorted_matrix)