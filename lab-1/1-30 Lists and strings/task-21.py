#21
result = lambda lst: list(map(str.upper, filter(lambda x: x.isalpha() and len(x) > 4
                                                and len(set(x.lower())) == len(x), lst)))
lst = ["hello", "world", "abcde", "test", "Python", "loop", "Uniqe"]
print (result(lst))