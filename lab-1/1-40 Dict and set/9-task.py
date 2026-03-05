def common_elements_all(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for current_set in sets_list[1:]:
        temp_common = set()
        for element in result:
            if element in current_set:
                temp_common.add(element)
        result = temp_common

    return result

data = [{'a', 'b'}, {'b', 'c'}, {'b', 'd'}]
result = common_elements_all(data)
print(result)

result_short = set.intersection(*data) # Короткий путь (не для задачи, а для жизни)
print(result_short)