# 9. How to reverse an array in place in Java? (solution)

test = [1,2,3,4,5,6,7]

def reverse(array:list)->list:
	arr = array.copy()
	for i in range(int(len(arr)/2)):
		oposite_extreme =len(arr)-1-i
		arr[i], arr[oposite_extreme] = arr[oposite_extreme], arr[i]
	return arr
	
print(test)
print(reverse(test))
