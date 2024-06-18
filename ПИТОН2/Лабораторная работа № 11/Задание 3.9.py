def separate_zeros_ones(sequence):
    zeros = []
    ones = []

    for num in sequence:
        if num == 0:
            zeros.append(num)
        elif num == 1:
            ones.append(num)

    return zeros + ones


# Пример использования
sequence = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
result = separate_zeros_ones(sequence)
print(result)
