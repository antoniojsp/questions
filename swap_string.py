str_1 = "uno"
str_2 = "dos"
print(str_1, str_2)

def swap_strings(str1, str2)-> str:
	str1 = str1 + str2
	str2 = str1[0:len(str1) - len(str2)]
	str1 = str1[len(str2):]

	return (str1, str2)

print(swap_strings(str_1, str_2))
