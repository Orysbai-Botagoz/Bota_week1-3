def pairwise_intersections(sets_list):
    if len(sets_list) < 2:
        return []

    result = []
    for i in range (len(sets_list) - 1):
        intersection = sets_list[i] & sets_list[i + 1]
        result.append(intersection)
    return result

data = [
    {1, 2, 3},
    {2, 3, 4},
    {3, 4, 5},
    {5, 6}
]
print(pairwise_intersections(data))