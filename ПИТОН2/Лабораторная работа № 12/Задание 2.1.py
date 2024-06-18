import numpy as np


M = 3
N = 4
matrix = np.random.randint(1, 10, size=(M, N))
print("Исходная матрица:")
print(matrix)


column_sums = np.sum(matrix, axis=0)


for i in range(N):
    print(f"Сумма элементов {i+1}-го столбца: {column_sums[i]}")