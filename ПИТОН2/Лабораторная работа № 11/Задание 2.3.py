X = [10, 5, 20, 8, 15, 30, 25, 18, 14, 12, 7, 29, 17, 22, 11]

max_element = X[0]
max_index = 0

for i in range(1, len(X)):
    if X[i] > max_element:
        max_element = X[i]
        max_index = i

print(f"Наибольший элемент списка X: {max_element}")
print(f"Порядковый номер наибольшего элемента: {max_index}")