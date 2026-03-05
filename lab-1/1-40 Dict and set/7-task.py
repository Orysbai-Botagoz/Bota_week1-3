symmetric_even = lambda s1, s2: set(filter(lambda x: x % 2 == 0, s1 ^ s2)) # ^ екі жүйенің бөлек мәндеріортақ мән жоқ
set_a = {1, 2, 4}
set_b = {4, 5, 6}

result = symmetric_even(set_a, set_b)
print (result)
