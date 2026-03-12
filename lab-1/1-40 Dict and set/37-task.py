import math
process_dict = lambda d: {
    k: (math.factorial(v) if v < 6 else v)
    for k, v in d.items()
}
data = {
    "a": 3,
    "b": 5,
    "c": 7,
    "d": 0
}
processed = process_dict(data)
print(processed)