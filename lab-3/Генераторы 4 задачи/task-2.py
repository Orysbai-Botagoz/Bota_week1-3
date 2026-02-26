def filter_words(words):
    for word in words:
        if len(word) > 4:
            if "а" in word:
                yield "c a"
            else:
                yield word
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print (w)