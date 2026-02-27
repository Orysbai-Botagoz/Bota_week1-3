def matrix_transform(matrix):

    result = (
        ("кратно 6" if col % 2 == 0 and col % 3 == 0 else "чётное" if col % 2 == 0 else "кратно 3" if col % 3 == 0 else col)
        for row in matrix
        for col in row
    )
    yield from result

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

for x in matrix_transform(matrix):
    print(x)