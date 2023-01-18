test = [i for i in range(0, 10)]


def is_even(num: int) -> bool:
    return num % 2 == 0


def remove_even(arr: list) -> list:
    result = []
    for i in arr:
        if not is_even(i):
            result.append(i)
    return result


# print(remove_even((test)))

def remove_even2(arr: list) -> list:
    for i in arr:
        if is_even(i):
            arr.remove(i)
    return arr


# print(remove_even2((test)))


b = [1, 2, 3, 4, 5, 6, 7]


def remove_element(arr: list, index: int) -> list:

    if len(arr) - 1 < index:
        print("Out of Index")
        return []

    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr.pop()
    return arr


# print(remove_element(b, 6))

a = [1, 2, 3, 4, 5, 12, 1, 2, 5, 6, 3, 7, 7, 7, 2, 2,3]
def remove_even3(arr: list) -> list:
    '''
    Complexity  n**2
    '''
    i = 0
    while i < len(arr):
        if is_even(arr[i]):
            remove_element(arr, i)
            continue
            i -= 1
        i += 1
    return arr


print(remove_even3(a))
