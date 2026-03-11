get_unique_overlap = lambda s1, s2, s3: (s1 & s2) - s3
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {4, 7, 8}
result = get_unique_overlap(set_a, set_b, set_c)
print (result)