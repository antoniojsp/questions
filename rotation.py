str1 = "BCDA"
str2 = "CDAB"

def rotation(str1:str, str2:str)->bool:
	# print(str1 in temp)
	result = False
	concat = str1 + str1
	for i in range(0, len(concat) - len(str2)):
		if concat[i:i+len(str2)] == str2:
			result = True 

	return result

print(rotation(str1, str2))