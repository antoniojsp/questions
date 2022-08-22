test = [2,12,-2,4,5,20,1,1,14,4,50,12]


def min_max(arr:list) -> tuple:
	if not arr:
		return (None, None)
	if len(arr) == 1:
		return (arr[0], arr[0])
		
	max_value = -float("inf")
	min_value = float("inf")

	for elem in arr:
		if elem > max_value:
			max_value = elem
		elif elem < min_value:
			min_value = elem
	return (min_value, max_value)

print(min_max(test))