# First Non-Repeating Integer in an Array
from collections import Counter

a = [2,1,1,1,1,1,9,9,1,51,2]


def first_non_rep(arr: list) -> int:
    result = -1
    count = Counter(arr)

    for i in count:
        if count[i] == 1:
            result = i
            break

    return result


# print(first_non_rep(a))
a = [1,1,1,1,1,9,9,1,51,1]

def first_non_rep1(arr:list)->int:
    i = 0
    result = -1

    while i < len(arr):
        current = arr[i]
        repeat = True #flag

        j = i + 1
        while j < len(arr):
            print(i, j)
            print("here",current, arr[j])
            if current == arr[j]:
                repeat = False
                break
            j += 1
        print()
        if repeat:
            result = current
            break
        i +=1

    return result
print(first_non_rep1(a))