#10
result = lambda s: sum(1 for w in s.split() if
                       any(c.isdigit() for c in w)
                       and not w[0].isdigit()
                       and len(w) >=5)
print (result("abc12 1test test123 ab12 x1y2z 12345 abcde9"))
