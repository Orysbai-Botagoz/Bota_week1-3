filter_dict = lambda d: dict(
    filter(
        lambda item: (
            len(item[1]) == len(set(item[1])) and
            all(len(s) > 3 for s in item[1])
        ),
        d.items()
    )
)
data = {
    "fruits": ["apple", "banana", "cherry"],
    "sets": ["code", "dev", "code"],
    "tech": ["python", "java", "rust"],
    "short": ["go", "lua", "c++"]
}

result = filter_dict(data)
print(result)