sort_dict_keys = lambda data: sorted(
    data.keys(),
    key=lambda k: (data[k] % 10, k),
)
input_data = {
    "banana": 15,
    "apple": 42,
    "cherry": 12,
    "date": 30
}
result = sort_dict_keys(input_data)
print(result)