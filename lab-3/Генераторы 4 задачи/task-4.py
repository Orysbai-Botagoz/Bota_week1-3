def squares(n):
    for x in range(1, n+1):
        if x % 2 == 0:
            yield "чётный квадрат"
        else:
            yield x ** 2
for x in squares(5):
    print (x)