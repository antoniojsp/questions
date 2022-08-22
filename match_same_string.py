from collections import Counter

def matching_same_char(string:str) -> list:
	# dictio = {}
	# for i in test:
	# 	if i in dictio:
	# 		dictio[i] += 1
	# 	else:
	# 		dictio[i] = 1
	if not string:
		return []

	count_char = Counter(list(string))

	result = []
	for i, j in count_char.items():
		if j > 1:
			result.append(i)
	return result

test = "abbcndaa"
print(matching_same_char(test))