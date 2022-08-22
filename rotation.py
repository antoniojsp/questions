str1 = "BCDA"
str2 = "CDAB"
temp = str1 + str1
print(temp)

print(str1 in temp)

for i in range(0, len(temp) - len(str2)):
	print(i)
	if temp[i:i+len(str2)] == str2:
		print(temp[i:i+len(str2)])
