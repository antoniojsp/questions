a = [1,2,3,4,1,7,5,10,4,7,3]


for i in range(0, len(a)):
	for j in range(i+1, len(a)):
		if a[i] == a[j]:
			print(a[i])
	