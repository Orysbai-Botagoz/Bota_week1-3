# 1
def analyze_text(text):
    text = text.lower()
    clean_text = ""
    for char in text:
        if "a" <= char <= "z" or char == " ":
            clean_text += char

    vowels = "aeiou"
    unique_vowels = set()
    for char in clean_text:
        if char in vowels:
            unique_vowels.add(char)
    num_unique_vowels = len(unique_vowels)

    words = clean_text.split()
    found_words = []
    seen = set()
    for word in words:
        if len(word) >= 5 and word[0] == word[-1] and word not in seen:
            found_words.append(word)
            seen.add(word)
    return (num_unique_vowels, " ".join(found_words))
print (analyze_text("level radar apple banana civic kayak level stats world refer"))

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

