def swap(arr, a, b):
	arr[b], arr[a] = arr[a], arr[b]
	return arr

def insertion_sort(arr:list)->list:
	arr_copy = arr.copy()
	i = 0
	for i in range(len(arr_copy)):
		j = i
		print(arr_copy, j)
		while j > 0:
			if arr_copy[j-1] > arr_copy[j]:
				print("swap")
				swap(arr_copy, j-1,j)
				print(arr_copy)
				j -= 1
			else:
				break

	return arr_copy

test = [5,4,12,1,3,1]

print(insertion_sort(test))