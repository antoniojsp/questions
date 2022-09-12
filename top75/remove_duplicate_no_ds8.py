test = [1,3,4,2,2,1,1,1,2,5,3,1,2,7,5,5,5,5777]


def delete_repeat_no_ds4(arr:list)->list:

	counter = 1
	arr.sort() #O(n. logn)
	current = arr[0]
	count = 0

	for i in range(1,len(arr)):
		if current != arr[i]:
			arr[counter] = arr[i]
			counter +=1
			current = arr[i]
			count +=1

	for i in range(len(arr)-counter):
		arr.pop()

	print(arr)

delete_repeat_no_ds4(test)






def move_left(arr:list, index:int)->list:
	for i in range(index, len(arr)-1):
		arr[i] = arr[i+1]
	arr.pop()
	return arr

def delete_repeat_no_ds3(array:list)->list:
	arr = array.copy()
	arr.sort()
	i = 0
	while i < len(arr)-1:
		if arr[i] == arr[i+1]:
			move_left(arr, i)
			continue
		i+=1

	return arr


def delete_repeat_no_ds(array:list)->list:
	arr = array.copy()
	arr.sort()
	solution = [arr[0]]
	for i in range(1,len(arr)):
		if solution[-1] != arr[i]:
			solution.append(arr[i])

	return solution

def delete_repeat_no_ds1(array:list)->list:
	arr = array.copy()
	arr.sort()
	current = arr[0]
	for i in range(1,len(arr)):
		if arr[i] == current:
			arr[i] = ""
		else:
			current = arr[i]

	current = 1
	for i in range(1, len(arr)):
		if arr[i] != "":
			arr[current] = arr[i]
			arr[i] = ""
			current += 1

	for i in range(len(arr)-current):
		arr.pop()

	return arr








