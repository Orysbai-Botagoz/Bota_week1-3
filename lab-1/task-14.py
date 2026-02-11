#14
result = lambda s: ','.join(
    filter(
        lambda w: len(set(w.lower())) > 3
                  and all(w.lower().count(v) <= 1 for v in "aeiou"),
        s.split()
    )
)
print (result("planet apple stone team loop read cloud"))