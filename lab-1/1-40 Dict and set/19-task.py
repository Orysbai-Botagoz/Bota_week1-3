def filter_by_digit_sum(nums):
    result = set()
    for num in nums:
        if num % 2 != 0:
            digit_sum = sum((int(digit)) for digit in str(abs(num)))
            if digit_sum % 2 == 0:
                result.add(num)
    return result

numbers = {11, 21, 33, 45, 57, 101}
result = filter_by_digit_sum(numbers)
print(result)