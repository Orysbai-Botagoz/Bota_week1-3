#4
result = lambda s: ' '.join(
    map(
        str.lower,
        filter(
            lambda word: sum(c.isupper() for c in word) == 1
            and not word[0].isupper()
            and not word[-1].isupper(),
            s.split()
        )
    )
)

print (result("heLlo WorLd thiS is a TeSt example"))