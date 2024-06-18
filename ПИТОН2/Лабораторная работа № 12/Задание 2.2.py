import numpy as np


matrix = np.random.randint(1, 10, size=(4, 3))
print("Исходная матрица:")
print(matrix)


row_sums = np.sum(matrix, axis=1)


for i, row_sum in enumerate(row_sums):
    print(f"Сумма элементов {i+1}-й строки: {row_sum}")