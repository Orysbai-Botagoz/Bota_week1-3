def process_numbers(numbers):
    pozitives = filter(lambda x: x >= 0, numbers)
    result = map(lambda n: n/2 if n % 2 == 0 else n*3+1, pozitives)
    yield from result
numbers = [5, -2, 8, 0, -7, 3]
for number in process_numbers(numbers):
    print(number)