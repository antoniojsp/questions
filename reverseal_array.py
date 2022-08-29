test = [1,2,3,4,5,6,7,8,9,10, 11]

def swap(arr, a, b)->list:
	array = arr[a], arr[b] = arr[b], arr[a]
	return array

def reverse_array(arr:list):
	copy_arr = arr.copy()
	# for i in range(0, int(len(copy_arr)/2)):
	# 	swap(copy_arr, i, len(copy_arr)-i-1)
	middle_element = int(len(copy_arr)/2)
	for i, j in zip(range(0,middle_element,1), range(len(copy_arr)-1,middle_element,-1)):
		swap(copy_arr, i, j)
	return copy_arr

print(test)
print(reverse_array(test))