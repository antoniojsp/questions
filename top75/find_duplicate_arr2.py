arr = [1,2,3,4,5,6,1]

#easy
duplicate_dict = {}
for i in arr:
	if i in duplicate_dict:
		duplicate_dict[i] +=1
	else:
		duplicate_dict[i] =1

for i, j in duplicate_dict.items():
	if j > 1:
		print(i)


