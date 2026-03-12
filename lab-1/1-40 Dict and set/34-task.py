def top_k_smallest_unique(nums, k):
    unique_nums = set(nums)
    sorted_unique = sorted(list(unique_nums))
    result_list = []
    limit = min(k, len(sorted_unique))
    for i in range(limit):
        result_list.append(sorted_unique[i])
    return set(result_list)
print(top_k_smallest_unique([1, 2, 3, 4, 5], 2))
print(top_k_smallest_unique([5, 1, 2, 1, 5, 3, 3, 4], 3))
print(top_k_smallest_unique([10, 20], 5))
print(top_k_smallest_unique([1, 2, 1, 2, 3, 4], 5))

