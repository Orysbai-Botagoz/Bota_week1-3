def sort_dict_by_value_length(d):
    items_list = []
    for key, value in d.items():
        items_list.append((key, value))

    items_list.sort(key=lambda x: (len(x[1]), x[0]))
    return items_list

data = {"cat": "meow", "dog": "woof", "bee": "bz"}
print(sort_dict_by_value_length(data))