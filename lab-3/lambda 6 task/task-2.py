words = ["арбуз", "кот", "машина", "дом", "ананас"]
result = list(sorted(words, key=lambda word: len(word)))
print (result)