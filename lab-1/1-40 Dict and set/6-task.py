def deep_sum(d):
    total = 0
    for value in d.values():
        if isinstance(value, (int, float)):
            total += value
        elif isinstance(value, list):
            total += sum(value)
        elif isinstance(value, dict):
            total += deep_sum(value) #рекурсия
    return total

data = {"x": 5, "y": [1, 2], "z": {"a": 10}}
print(deep_sum(data))
