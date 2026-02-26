numbers = [5, 12, 7, 20, 33, 8]
result = list(filter(lambda num: num % 2 == 0 and num > 10, numbers))
print (result)
