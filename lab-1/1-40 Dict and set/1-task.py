#1
def invert_unique(d):
    new_dict = {}
    for key, value in d.items():
        if value not in new_dict:
            new_dict[value] = []
        if key not in new_dict:
            new_dict[value].append(key)
    return new_dict
d = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1, 'f': 2, 'b': 2}
print(invert_unique(d))
