def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length ] = []
        if word not in result[length]:
            result[length].append(word)
    return result


data = ["apple", "lemon", "banana", 'chery']
print (group_by_length(data))
