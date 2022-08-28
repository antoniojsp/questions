def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]
	return arr


test = [5,4,12,1,3,1]


# for i in range(len(test)):
# 	if test[i] > test[i+1]:
# 		swap(test, i, i+1)


i = 0
while i < len(test)-1:
	j = i
	while j < len(test)-1:
		if test[i] > test[i+1]:
			swap(test, i, i+1)
			i -= 1
		i +=1 

print(test)