def top_k_frequent(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    items = list(counts.items())

    items.sort(key=lambda x: (-x[1], x[0])) #x[0] по возрастанию, если частоты равны

    result_list = items[:k]
    final_set = set()
    for val, freq in result_list:
        final_set.add(val)
    return list(final_set)

data = [10, 20, 10, 20, 30, 30, 5, 5, 5]
print(top_k_frequent(data, 3))
