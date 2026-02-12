#22
def group_by_parity_and_sort(nums):
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    evens.sort()
    odds.sort()
    return evens+odds

nums = [5, 2, 9, 4, 7, 8, 1, 6]
print(group_by_parity_and_sort(nums))
