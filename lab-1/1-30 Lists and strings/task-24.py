def longest_increasing_sublist(nums):
    if not nums:
        return []
    max_sublist = []
    curr_sublist = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr_sublist.append(nums[i])
        else:
            if len(curr_sublist) > len(max_sublist):
                max_sublist = curr_sublist
            curr_sublist = [nums[i]]
    if len(curr_sublist) > len(max_sublist):
        max_sublist = curr_sublist
    return max_sublist
nums = [1, 2, 2, 3, 4, 1, 2, 3, 4, 5]
print(longest_increasing_sublist(nums))

