clean_dict = lambda d: dict(
    filter(
        lambda item: not (item[1] % 3 == 0 or len(item[0]) % 2 == 0),
        d.items()
    )
)

data = {
    "apple": 10,
    "pear": 9,
    "banana": 12,
    "kiwi": 8,
    "cherry": 7
}
result = clean_dict(data)
print(result)