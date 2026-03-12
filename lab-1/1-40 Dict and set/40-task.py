def analyze_dict_keys(d):
    unique_chars = set()

    to_exclude = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    for key in d.keys():
        if isinstance(key, str): #проверка является ли это строкой
            if not any(char.isdigit() for char in key):

                for char in key:
                    if char not in to_exclude:
                        unique_chars.add(char)
    return unique_chars
print(analyze_dict_keys({"hello!": 1, "bit_2": 2}))
