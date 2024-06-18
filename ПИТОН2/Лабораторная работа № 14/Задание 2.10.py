def create_dict(keys, values):

    if len(keys) != len(values):
        raise ValueError("Длины списков не совпадают")
    return dict(zip(values, keys))



keys = ['a', 'b', 'c']
values = [1, 2, 3]
result_dict = create_dict(keys, values)
print(result_dict)