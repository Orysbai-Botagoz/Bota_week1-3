#6
result = lambda s: list(filter (lambda w: len(w) >= 4
                                and w.isalpha()
                                and len(set(w.lower())) == len(w), s.split()))
#s.split() — разбиваем строку на слова
print (result("home test book abc1 AbCd lamp moon"))