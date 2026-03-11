get_top_keys = lambda d: sorted(d, key=lambda k: (d[k], len(k)))[:3]
data = {
    "banana": 10,
    "apple": 10,
    "kiwi": 5,
    "cherry": 20
}
result = get_top_keys(data)
print(result)