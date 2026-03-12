def partition_by_sum_parity(s):
    even_sum_set = set()
    odd_sum_set = set()
    for num in s:
        current_sum = 0
        for digit in str(abs(num)):
            current_sum += int(digit)
        if current_sum % 2 == 0:
            even_sum_set.add(num)
        else:git
            odd_sum_set.add(num)
    return (even_sum_set, odd_sum_set)
input_numbers = {12, 34, 56, 11, 20}
even, odd = partition_by_sum_parity(input_numbers)
print (f"Четная сумма: {even}")
print (f"Нечетная сумма: {odd}")