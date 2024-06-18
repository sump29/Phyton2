import numpy as np


M = 4
N = 5
matrix = np.arange(M*N).reshape(M, N)
print("Исходная матрица:")
print(matrix)


for i in range(len(matrix)):
    if i % 2 == 0:
        print(matrix[i])
    else:
        print(matrix[i, ::-1])