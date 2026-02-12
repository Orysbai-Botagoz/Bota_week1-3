result = lambda nums: list(map(
    lambda x: x ** 2,
    filter(
        lambda x: (x % 3 == 0 or x % 5 == 0)
        and x % 15 != 0
        and len(str(x)) % 2 == 1,
        nums
    )
))
print (result([3, 5, 15, 33, 123, 555, 7, 10]))