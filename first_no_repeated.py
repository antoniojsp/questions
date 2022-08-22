from collections import Counter

test = "aaddbbajdjdjdkkk"


def first_no_repeat(string:str) -> str:
	result = ""
	count_char = Counter(string)
	for char in string:
		if count_char[char] == 1:
			return char
	return ""

print(first_no_repeat(test))