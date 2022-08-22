a = [1,2,3,5,6,7,8]

def find_missing(arr:list)->int:
	if not arr:
		return -1

	lenght = arr[-1]
	list_sum = sum(a)
	sum_needed = (lenght*(lenght+1)/2)

	return int(sum_needed - list_sum)

print(find_missing(a))