# First Non-Repeating Integer in an Array
from collections import Counter

a = [1,1,1, 2,2, 3, 3, 5, 5, 6,6, 7,7, 8, 8, 8,9]


def first_non_rep(arr: list) -> int:
    result = -1
    count = Counter(arr)

    for i in count:
        if count[i] == 1:
            result = i
            break

    return result


# print(first_non_rep(a))

