def group_by_last_letter(words):
    result = {}
    for word in words:
        if not word:
            continue
        last_letter = word[-1]
        if last_letter not in result:
            result[last_letter] = []
        if word not in result[last_letter]:
            result[last_letter].append(word)
    return result
words_list = ["apple", "banana", "pear", "orange", "apple", "grape"]
result = group_by_last_letter(words_list)
print(result)