#23
def is_prime(n): #жай санба соны тексеруге
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
result = lambda lst: [x for i, x in enumerate(lst) #индекс и значение
                      if x % 2 == 1
                      and x > sum(lst)/len(lst)
                      and is_prime(i) == True]
lst = [4, 7, 10, 15, 2, 9, 8, 13]
print(result(lst))