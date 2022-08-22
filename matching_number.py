a = [3,1,2,3,4,1,7,5,10,4,7,3]

def matching_number(arr:list) -> list:
	'''
	It's not O(n^2) per since eve
	'''
	arr.sort()
	result = []
	for i in range(0, len(a)):
		for j in range(i+1, len(a)):
			if a[i] == a[j]:
				result.append(a[i])
	return result

print(matching_number(a))

	