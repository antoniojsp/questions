a = [3,1,2,3,4,1,7,5,10,4,7,3]

def matching_number(arr:list) -> list:
	'''
	It's not O(n^2) per since eve
	'''
	result = set()
	for i in range(0, len(arr)):
		
		for j in range(i+1, len(arr)):
			if arr[i] == arr[j]:
				result.add(arr[i])
				
	return result

print(matching_number(a))

	