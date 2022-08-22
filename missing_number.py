a = [1,2,3,5,6,7,8]

def find_missing(arr:list)->int:
	if not arr:
		return -1

	upper_number = arr[-1]
	arr_sum = sum(arr)
	range_sum = (upper_number*(upper_number+1)/2) # 


	return int(range_sum - arr_sum)

print(find_missing(a))