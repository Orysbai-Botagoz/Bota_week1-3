#15
def word_pattern_sort(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    length_dict = {} #длина слова = список слов этой длины
    for word in words:
        l = len(word)
        if l not in length_dict:
            length_dict[l] = []
        length_dict[l].append(word)

    result = []

    for l in sorted(length_dict):
        group = length_dict[l]
        group_sorted = sorted(group, key=lambda x: (-sum(1 for c in x if c in vowels), x))
        result.extend(group_sorted) #расширяет текущий список, увеличивая его длину, модифицируя его «на месте» (in-place) и возвращая
    return result
print (word_pattern_sort("apple bee dog tree read loop cloud"))



