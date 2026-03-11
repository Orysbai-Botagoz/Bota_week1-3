def update_counts(d, items):
    for item in items:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

my_dict = {'apple': 2, 'banana': 1}
my_items = ['apple', 'orange', 'apple']
result = update_counts(my_dict, my_items)
print (result)