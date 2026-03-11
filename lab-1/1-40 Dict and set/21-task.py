def count_leaf_values(d):
    count = 0
    stack = [d]
    while stack:
        current_dict = stack.pop() # Достаем текущий словарь из стека
        for value in current_dict.values():
            if isinstance(value, dict):
                stack.append(value)
            else:
                count += 1
    return count
data = {
    "a": 1,
    "b": [1, 2, 3], # список — это один "лист"
    "c": {
        "d": 2,
        "e": {
            "f": 3
        }
    }
}
print(count_leaf_values(data))
