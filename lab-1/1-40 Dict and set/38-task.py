def multi_symmetric_difference(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for i in range(1, len(sets_list)):
        result = result ^ sets_list[i] #^ - difference
    return result
data = [
    {1, 2, 3},
    {2, 3, 4},
    {3, 4, 5},
]
print(multi_symmetric_difference(data))
