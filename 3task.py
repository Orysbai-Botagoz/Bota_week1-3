def top_k_words(text, k):
    lower_text = text.lower()
    clean_text = ""
    for char in lower_text:
        if "a" <= char <= "z" or char == " ":
            clean_text += char
    counts = {}
    words = clean_text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    items = list(counts.items())
    items.sort(key=lambda x: (-x[1], x[0]))

    result = list()
    for i in range(min(k, len(items))):
        result.append(items[i][0])
    return result


print(top_k_words("Apple, banana! Apple orange banana apple. Orange banana?", 3))