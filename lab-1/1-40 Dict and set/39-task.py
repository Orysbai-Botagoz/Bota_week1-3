vowels = "aeiouAEIOU"
sort_keys = lambda d: sorted(
    d.keys(),
    key=lambda k: (
        sum(1 for char in k if char in vowels),
    -d[k]
    )
)
data = data = {
    "apple": 10,
    "banana": 5,
    "kiwi": 15,
    "orange": 5
}
print(sort_keys(data))