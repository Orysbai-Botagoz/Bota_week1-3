#2
filter_logic = lambda s: set(filter(lambda x: x > sum(s)/len(s) and x % 2 != 0 and x % 5 != 0, s))
numbers = {1, 2, 5, 7, 10, 11, 13, 15, 20, 23}
print(filter_logic(numbers))