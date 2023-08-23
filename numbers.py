def positive_count(a, b, c):
    # The function returns True if at least two of the arguments are positive.

    positive_nums = [num for num in (a, b, c) if num >= 0]
    return len(positive_nums) >= 2


result = positive_count(10, -5, 2)
print(result)
