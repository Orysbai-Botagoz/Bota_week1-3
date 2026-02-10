#8
result = lambda s: ' '.join(map(
    lambda w:
    w if any(c.isdigit() for c in w)
    else "VOWEL" if w[0].lower() in "aeiou"
    else "CONSONANT",
          s.split()
))
print (result("apple banana tree 4you Orange x7 test"))