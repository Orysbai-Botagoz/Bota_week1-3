def remove_elements_with_common_digits(s):
    digit_counts = {}
    for num in s:
        unique_digits_in_num = set(str(abs(num)))
        for digit in unique_digits_in_num:
            digit_counts[digit] = digit_counts.get(digit, 0) + 1
    common_digits = {digit for digit, count in digit_counts.items() if count > 1}

    result = set()
    for num in s:
        num_digits = set(str(abs(num)))
        if not (num_digits & common_digits):
            result.add(num)
    return result

numbers = {12, 34, 56, 17}
print(remove_elements_with_common_digits(numbers))