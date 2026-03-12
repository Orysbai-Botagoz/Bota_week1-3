def all_subsets_of_size_k(s, k):
    elements = list(s)
    n = len(elements)
    if k > n or k < 0:
        return []
    if k == 0:
        return [set()]
    result = []

    def backtrack(start, current_subset):
        if len(current_subset) == k:
            result.append(set(current_subset))
            return
        for i in range(start, n):
            current_subset.append(elements[i])
            backtrack(i + 1, current_subset)
            current_subset.pop() #pop() — он удаляет 2. Список снова: [1].
    backtrack(0, [])
    return result
my_set = {1, 2, 3, 4}
k = 2
print(all_subsets_of_size_k(my_set, k))