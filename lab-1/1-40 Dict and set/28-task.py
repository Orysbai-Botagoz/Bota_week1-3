def sorted_unique_chars(strings):
    unique_chars = set()
    for string in strings:
        for char in string:
            if not char.isdigit() and char != ' ':
                unique_chars.add(char)

    return sorted(list(unique_chars))

data = ["hello 123", "world!", "python 3.11"]
print(sorted_unique_chars(data))