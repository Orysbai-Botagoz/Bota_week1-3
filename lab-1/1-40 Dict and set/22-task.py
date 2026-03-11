filter_sets = lambda s1, s2: {x for x in s1 if x > (sum(s2)/ len(s2)) and x not in s2}
set_a = {10, 20, 30, 40, 5}
set_b = {10, 15, 25}
result = filter_sets(set_a, set_b)
print(result)