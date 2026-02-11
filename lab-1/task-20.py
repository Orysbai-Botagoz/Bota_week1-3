def max_subarray_sum(nums, k):
    max_sum = None
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        if all(x > 0 for x in window):
            s = sum(window)
            if max_sum is None or s > max_sum:
                max_sum = s
    return max_sum
nums = [1, 2, 3, -1, 4, 5, 0, 6]
print(max_subarray_sum(nums, 2))
