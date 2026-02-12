#2
def words(text):
    new_text = text.split()
    filtered_text = list(filter(lambda x: not any(ch.isdigit() for ch in x), new_text))
    reverse_text = list(map(lambda s: s[::-1], filtered_text))
    result_text = ""
    for word in reverse_text:
        if len(word) % 2 == 0:
            result_text += word + " "
    return result_text.strip()
print (words("hello abc123 world test44 noon even 2468 python code"))