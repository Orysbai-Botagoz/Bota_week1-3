#9
def alternate_case_blocks(text, n):
    result = ""
    block_number = 0
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if block_number % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()
        block_number += 1
    return result
print (alternate_case_blocks("abcdefghijk", 3))