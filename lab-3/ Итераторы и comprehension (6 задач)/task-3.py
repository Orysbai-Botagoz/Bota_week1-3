words = ["кот", "машина", "ананас", "дом", "телефон"]
result = [word for word in words if len(word) > 4 and not "а" in word]
print(result)