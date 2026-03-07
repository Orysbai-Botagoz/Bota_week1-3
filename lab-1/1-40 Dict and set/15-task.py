filter_dict = lambda d: {
    k: v for k, v in d.items()
    if v >= (sum(d.values()) / len(d) if d else 0)
       and v % 2 != 0
}

data = {"a": 1, "b": 10, "c": 5, "d": 3, "e": 8}
print (filter_dict(data))