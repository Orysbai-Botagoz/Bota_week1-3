#27
result = lambda lst: sorted(lst, key=lambda x: (-len(x), x) # сначала по убыванию длины, потом по алфавиту
                            )[:5] # оставляем только первые 5 элементов
words = ["apple", "banana", "kiwi", "strawberry", "pear", "grape", "melon"]
print(result(words))
