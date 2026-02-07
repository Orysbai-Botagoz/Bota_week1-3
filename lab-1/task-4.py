#4
filter_words = lambda text: " ".join( #list to str
        word.lower()
        for word in text.split()
        if sum(1 for c in word[1:-1] if c.isupper()) == 1)
print (filter_words("heLlo WorLd thiS is a TeSt example"))

filter_words = lambda text: " ".join(  # list → str
    word.lower()
    for word in text.split()
    if sum(1 for c in word[1:-1] if c.isupper()) == 1
)

print(filter_words("heLlo WorLd thiS is a TeSt example"))