result = lambda s: list(filter(lambda w:
                               len(w) > 3
                               and w[0].lower() == w[-1].lower()
                               and w.lower() != w.lower()[::-1],
                               s.split()))
print (result("level test radar abca anna civic kayak alpha omega"))