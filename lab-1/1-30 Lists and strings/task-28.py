#28
def moving_average(nums, k):
    result = []
    n = len(nums)
    for i in range(n - k + 1):
        window = nums[i:i + k]
        if all(x > 0 for x in window):
            average = sum(window) / k
            result.append(average)
    return result
nums = [1, 2, 3, -1, 4, 5]
k = 3
print(moving_average(nums, k))