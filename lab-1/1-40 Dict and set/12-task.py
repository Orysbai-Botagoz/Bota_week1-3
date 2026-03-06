filterd_set = lambda s: set(filter(lambda w: w.isalpha() and len(w) > 4 and len(set(w)) == len(w), s))
data = {"apple", "lemon", "banana", 'chery', '123', 'jfoej23'}
print (filterd_set(data))
