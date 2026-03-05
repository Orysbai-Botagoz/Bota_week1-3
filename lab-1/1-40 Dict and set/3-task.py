#3
d1 = {"яблоки": 5, "бананы": 2}
d2 = {"яблоки": 3, "груши": 4}
def merge_dicts_sum(d1, d2):
    result = dict()
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value
    return result

print(merge_dicts_sum(d1, d2))