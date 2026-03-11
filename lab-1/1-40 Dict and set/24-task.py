def union_of_filtered_sets(sets_list):
    result = set()
    for current_set in sets_list:
        for num in current_set:
            if num > 10 and num % 2 != 0:
                result.add(num)
    return result
data = [
    {5, 11, 12, 13},
    {21, 30, 7},
    {11, 99, 100}
]
print(union_of_filtered_sets(data))