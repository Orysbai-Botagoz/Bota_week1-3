def filter_sets(sets_list):
    filtered_result = []
    for i in sets_list:
        if len(i) > 3 and (min(i) >= 0):
            for number in i:
                if number % 2 == 0:
                    filtered_result.append(i)
                    break

    return filtered_result

sets_list = [{1, 2, 3, 4}, {10, 20, 30, 40}, {-1, 5, 6, 7, 8}, {1, 3, 5, 7, 9}]
print(filter_sets(sets_list))