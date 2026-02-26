def infinite_numbers():
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i
        i += 1
gen = infinite_numbers()
for _ in range (15):
    print (next(gen))