#29
result = lambda lst1, lst2: [x for x in lst1
                             if x not in lst2
                             and x > sum(lst1)/len(lst1)]
lst1 = [1, 5, 8, 10, 12]
lst2 = [5, 12]
print(result(lst1, lst2))