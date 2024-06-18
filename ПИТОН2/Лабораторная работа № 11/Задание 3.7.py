def rearrange_numbers(nums):
    negatives = [num for num in nums if num < 0]
    positives = [num for num in nums if num >= 0]

    nums.clear()

    nums.extend(negatives)
    nums.extend(positives)


# Пример использования
original_list = [5, -3, 8, -2, -10, 4, 7, -6, 1, 0, -9, 2]
rearrange_numbers(original_list)
print(original_list)
