
filter_prime_odd = lambda data: {
    k: v for k, v in data.items()
    if len(k) % 2 != 0 and v > 1 and all(v % i != 0 for i in range (2, int(v**0.5) + 1))

}
input_data = {
    "apple": 7,
    "pear": 5,
    "banana": 11,
    "kiwi": 4,
    "egg": 13,
    "sky": 9
}
result = filter_prime_odd(input_data)
print(result)