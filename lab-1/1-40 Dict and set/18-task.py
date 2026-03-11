def sort_dict_by_value_sum(d):
    aggregated_list = []
    for k, v in d.items():
        total_sum = sum (v)
        aggregated_list.append((k, total_sum))
    sorted_result = sorted(aggregated_list, key=lambda x: (-x[1], x[0]))
    return sorted_result
data = {
    "apple": [10, 20],   # Сумма: 30
    "banana": [15, 15],  # Сумма: 30
    "cherry": [5, 5]     # Сумма: 10
}
result = sort_dict_by_value_sum(data)
print (result)