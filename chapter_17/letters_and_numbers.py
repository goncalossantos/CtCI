def letters_numbers_brute_force(array: str) -> int:
    max_len = 0
    for i in range(len(array)):
        count_digit = 0
        count_char = 0
        for j in range(i):
            if array[j].isdigit():
                count_digit += 1
            else:
                count_char += 1
        if count_char == count_digit:
            max_len = max(max_len, count_char + count_char)
        for j in range(i, len(array)):
            if array[j].isdigit():
                count_digit += 1
            else:
                count_char += 1
            if array[j - i].isdigit():
                count_digit -= 1
            else:
                count_char -= 1
            if count_char == count_digit:
                max_len = max(max_len, count_char + count_char)
    return max_len


def letters_numbers(array: str) -> int:
    max_len = 0
    difference = {}
    current = 0
    for i in range(len(array)):
        if array[i].isdigit():
            current -= 1
        else:
            current += 1
        if current in difference:
            max_len = max(max_len, i - difference[current])
        else:
            difference[current] = i
    return max_len
