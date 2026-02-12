def replace_every_nth(text, n, char):
    result = ""
    for i in range (len(text)):
        current = text[i]
        if current != " ":
            start = i
            while start > 0 and text[start - 1] != " ":
                start -= 1

            end = i
            while end < len(text) and text[end - 1] != " ":
                end += 1

            word_length = end - start + 1
        else:
            word_length = 0

        if (i+1) % n == 0 and current != " " and not current.isdigit() and word_length >= 3:
            result += char
        else:
            result += current
    return result
print(replace_every_nth("hello to my world 12345", 3, "*"))

