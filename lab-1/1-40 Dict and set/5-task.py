top_keys = lambda d: sorted(d.keys(),
                            key=lambda k: (-d[k], k)
                            )[:5]
data = {"a": 10, "b": 50, "c": 50, "d": 5}

print (top_keys(data))

