# 11. How to Print duplicate characters from String? (solution)

from collections import Counter

test = ["Programming", "Java", "Antonio"]

def find_duplicate_char11(string:str)->list:
	count = Counter(string)
	for key, val in count.items():
		if val > 1:
			print(f"Char:{key}, Times:{val}")



# print(find_duplicate_char11(test[2]))

def find_duplicate_char12(string:str)->list:
	#65-122
	chars = [0]*(122-65)

	result = []
	resultado = set()
	for i in string:
		chars[ord(i)-65] +=1
		if chars[ord(i)-65] > 1:
			resultado.add(i)

	print(resultado)

	for order, times in enumerate(chars):
		if times > 1:
			result.append((chr(order+65), times))

	return result



print(find_duplicate_char12(test[0]))