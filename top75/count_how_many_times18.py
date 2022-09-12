# 18. How to count the occurrence of a given character in String? (solution)

test = 'Today is Monday'

def count_char(string:str, character:chr)->int:
	'''
	o(n)
	'''
	count = 0
	for i in string:
		if i == character:
			count+=1

	return count

print(count_char(test, "a"))