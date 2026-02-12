def common_unique_chars(s1, s2):
    result = ""
    for char in s1:
        if char != " " and not char.isdigit():
            if char in s2:
                if char not in result:
                    result += char
    return result
print(common_unique_chars("a1b cdeff", "fabc 123"))