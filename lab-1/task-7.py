#7
def palindrome_words(text):
    new_text = ""
    for char in text:
        if ("a" <= char <= "z") or char == " ":
            new_text += char
    words = new_text.split()
    result = []
    for word in words:
        if word == word[::-1] and len(word) >= 3 and word not in result:
            result.append(word)
    result = sorted(result, key = lambda x: (-len(x), x))
    return result

print (palindrome_words("Level, radar! civic deed noon kayak level"))

