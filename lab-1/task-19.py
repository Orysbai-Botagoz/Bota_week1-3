result = lambda a, b : [x for x, y in zip(a, b) #zip(a, b) → создаёт пары элементов с одинаковыми индексами (a[i], b[i])
                        if x == y and x % 2 == 0]
a = [2, 3, 4, 6, 7, 8]
b = [2, 5, 4, 5, 7, 8]

print(result(a, b))