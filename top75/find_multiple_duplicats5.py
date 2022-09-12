# 5. How to find duplicate numbers in an array if it contains multiple duplicates?

class EmptyArray(Exception):
	def __init__(self, message):
		print(message)


def remove_duplicate2(arr:list)->list:
	arr_sorted = sorted(arr)

	result = [arr_sorted[0]]
	for i in range(1,len(arr_sorted)):
		if arr_sorted[i] != result[-1]:
			result.append(arr_sorted[i])			

	return result
		
		
test = [1,4,1,2,3,3,3,2,3,4,1,1,2,2]

print(remove_duplicate2(test))

def remove_duplicate1(arr:list)->list:

	if not arr:
		raise EmptyArray("Empty array.")

	count = {}
	for i in arr:
		count[i] = True

	return sorted([i for i in count.keys()])

test = [1,4,2,3,4]
print(remove_duplicate1(test))




