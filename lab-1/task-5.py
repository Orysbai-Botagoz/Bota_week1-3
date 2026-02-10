#5
def compress_text(text):
    new_text = ""
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i-1].lower():
            count += 1
        else:
            new_text += text[i-1]
            if count > 1:
                new_text += str(count)
            count = 1
    new_text += text[-1]
    if count > 1:
        new_text += str(count)
    return new_text
print (compress_text("aaBBcDDD"))
