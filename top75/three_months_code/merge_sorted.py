a = [1, 2, 2, 3, 4, 5, 5, 6, 7,8,9]
b = [1, 3, 4, 5, 6, 7, 10]


def merge_and_sort(arr_x: list, arr_y: list) -> list:
    '''
    O(n)
    '''
    i = 0
    j = 0

    result = []
    while not i == len(arr_x) or not j == len(arr_y):

        if i >= len(arr_x):
            result.extend(arr_y[j:len(arr_y)])
            break
        elif j >= len(arr_y):
            result.extend(arr_x[i:len(arr_x)])
            break

        if arr_x[i] < arr_y[j]:
            result.append(arr_x[i])
            i += 1
        elif arr_x[i] > arr_y[j]:
            result.append(arr_y[j])
            j += 1
        else:
            result.append(arr_x[i])
            result.append(arr_y[j])
            i += 1
            j += 1

    return result


print(merge_and_sort(a, b))
print(sorted(a + b))
