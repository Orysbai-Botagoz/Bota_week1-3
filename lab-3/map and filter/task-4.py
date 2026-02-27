numbers = [0, 5, 12, 7, 20, -3, 8]
pozitivies = list(filter(lambda n: n > 5, numbers))
result = list(map(lambda n: n / 2 if n % 2 == 0 else n * 3, pozitivies))
print(result)

#or

result = list(map(lambda x: x/2 if x % 2 == 0 else x*3,
filter(lambda x: x > 5, numbers)))
print(result)
