#25
result = lambda lat: list(map(
    lambda x: sum(x)/len(x), filter(
        lambda x: len(x) >= 3 and sum(x) % 2 == 0, lst

    )))
lst = [[1, 2, 3], [4, 5], [2, 2, 2, 2], [1, 3, 5], [10, 20, 30]]
print(result(lst))