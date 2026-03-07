def invert_dict_strict(d):
    counts = {}
    for value in d.values():
        counts[value] = counts.get(value, 0) + 1 #(Ключ, который мы ищем,Значение, которое вернется, если ключа нет в словаре)

    inverted = {}
    for key, value in d.items():
        if counts[value] == 1:
            inverted[value] = key
    return inverted
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(invert_dict_strict(data))