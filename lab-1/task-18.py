#18
def flatten_and_filter(lst):
    result = []
    stack = lst[:] #копия списка для обработки
    i = 0
    while i < len(stack):
        item = stack[i]
        if type(item) == list:
            stack = stack[:i] + item + stack[i+1:]
        elif type(item) == int:
            if item > 0 and item % 4 != 0 and item > 9:
                result.append(item)
            i += 1
        else:
            i += 1
    return sorted(result)
lst = [1, [12, -5, [20, 25]], 7, [44, [16, 15]]]
print(flatten_and_filter(lst))