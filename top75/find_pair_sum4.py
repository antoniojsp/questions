from collections import Counter

arr = [1,2,3,4,5,6,7,8]

def find_pair_1(value:int, arr:list)->list:
	'''
	Find all the pairs and do not repeat values
	it's 0(n^2)
	'''
	result = []
	arr.sort()
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] + arr[j] == value:
				result.append((arr[i], arr[j]))

	return result

# print(find_pair_1(10, arr))

def count_index(val, arr):
	result = {}

	for i in range(len(arr)):
		if arr[i] not in result:
			result[arr[i]] = [i]
		else:
			result[arr[i]].append(i)

	return result

arr = [1,2,3,4,5,5,6,7,8]

def find_pair_2(value:int, arr:list)->list:
	'''
	Steps:
	create a dictionary for values_seek
	Check each value and calculate the pair (value[i])
	if not present, add he result in the dictionary indicating that we are looking for that value
	if present, add the pair to the result
	'''	

	result = []
	values_seek= {}
	for i in range(len(arr)):
		seek = value - arr[i]
		if seek not in values_seek:
			values_seek[arr[i]] = True
		else:
			result.append((arr[i], seek))

	return result

print(find_pair_2(10,arr))







