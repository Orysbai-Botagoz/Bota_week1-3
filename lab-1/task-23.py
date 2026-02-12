#23
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
result = lambda lst: [lambda x: x % 2 == 1 and x > sum(x)/len(x) and is_prime(x) == True]
lst = [4, 7, 10, 15, 2, 9, 8, 13]
print(result(lst))