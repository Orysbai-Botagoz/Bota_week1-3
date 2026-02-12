#16
def transform_list(nums):
    result = []
    for num in nums:
        if num < 0:
            continue
        if num % 2 == 0:
            result.append(num ** 2)
        elif num > 10:
            sum_digits = sum(int(d) for d in str(num))
            result.append(sum_digits)
        else:
            result.append(num)
    return result
nums = [4, -3, 15, 7, 12, -8, 11, 2]
print(transform_list(nums))