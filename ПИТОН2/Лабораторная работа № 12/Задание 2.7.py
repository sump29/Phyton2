def count_elements_divisible_by_k(matrix, k):
    count = 0
    for row in matrix:
        for elem in row:
            if elem % k == 0:
                count += 1
    return count

def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k = 2

print("Исходная матрица:")
print_matrix(matrix)

result = count_elements_divisible_by_k(matrix, k)
print(f"Число элементов матрицы, кратных {k}: {result}")