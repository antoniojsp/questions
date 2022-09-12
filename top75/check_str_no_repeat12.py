from collections import Counter

def check_norepeat(string:str)->chr:
	'''
	Counter o(n)
	check for the first no repetitive o(n)
	'''
	count_string = Counter(string)

	for i in string:
		if count_string[i] == 1:
			return i
	return ""


test = "abcdefghija"

print(check_norepeat(test))


