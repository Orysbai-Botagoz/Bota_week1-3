#26
def remove_duplicates_keep_last(nums):
    seen = set()
    result = []
    for num in reversed(nums):
        if num not in seen:
            result.append(num)
            seen.add(num)
    result.reverse()
    return result
nums = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates_keep_last(nums))
