import time

test = [44,23,1,2,357,33,1,1,3,2,14,4]


def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]
	return arr
 
def bubbble_sort(arr:list)->list:
	'''
	It doesn't change the original array
	'''	
	arr_copy = arr.copy()

	for j in range(len(arr_copy)-1):
		swapped = False
		for i in range(len(arr_copy)-1):
			if arr_copy[i] > arr_copy[i+1]:
				swap(arr_copy, i, i+1)
				swapped = True
				
		if not swapped:
			break

	return arr_copy


print(bubbble_sort(test))
print(test)
