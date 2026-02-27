words = ["кот", "машина", "арбуз", "дом", "ананас"]
result = [(lambda w: (word.upper() if len(word) > 4 else "short") + ("*" if "а" in word else ""))(word) for word in words]

print (result)