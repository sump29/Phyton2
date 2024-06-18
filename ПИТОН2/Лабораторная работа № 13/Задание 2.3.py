def sum_numbers_in_range(nums, start_idx, end_idx):
    num_list = nums.split()
    start_idx = max(0, start_idx)
    end_idx = min(len(num_list), end_idx + 1)

    total_sum = 0
    for num in num_list[start_idx:end_idx]:
        total_sum += int(num)

    return total_sum



nums_input = input("Введите набор целых чисел, разделенных пробелами: ")


start_idx, end_idx = map(int, input("Введите два целых числа X и Y (индексы): ").split())

result = sum_numbers_in_range(nums_input, start_idx, end_idx)
print(result)