numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda num: num ** 2 if num % 2 == 0 else num * 3, numbers))
print (result)