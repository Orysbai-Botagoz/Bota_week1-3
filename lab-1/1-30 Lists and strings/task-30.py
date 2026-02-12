#30
def analyze_strings_list(words):
    result = []
    seen = set()
    for word in words:
        if any (c.isdigit() for c in word):
            continue
        if len(word) % 2 == 0:
            transdormed = word[::-1]
        else:
            transdormed = word.upper()
        if transdormed not in seen:
            seen.add(transdormed)
            result.append(transdormed)


    return result

words = ["hello", "world", "abc123", "python", "hello", "data", "ai"]
print(analyze_strings_list(words))


