process_dict = lambda d: {
    k: sorted([x for x in v if x % 2 != 0])
    for k, v in d.items()
    if any(x % 2 != 0 for x in v)
}
data = {
    "numbers": [4, 1, 3, 2, 5],
    "only_even": [2, 4, 6],
    "mixed": [10, 11, 7, 8],
    "empty": []
}
print(process_dict(data))