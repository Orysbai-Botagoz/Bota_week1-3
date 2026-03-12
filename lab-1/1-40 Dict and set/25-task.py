import math
process_data = lambda data: {
    k: math.prod(pos_nums)
    for k, v in data.items()
    if (pos_nums := [x for x in v if x > 0])
}
input_dict = {
    "a": [1, 2, -3, 4],
    "b": [-1, -5, 0],
    "c": [10, 5],
    "d": []
}
result = process_data(input_dict)
print(result)