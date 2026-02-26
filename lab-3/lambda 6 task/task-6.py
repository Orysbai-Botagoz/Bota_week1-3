numbers = [0, -3, 5, -7, 8]
result = [(lambda x: "положительное" if x > 0 else "отрицательное" if x < 0 else "ноль")(x) for x in numbers]
print (result)