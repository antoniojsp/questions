test = "Maria La Del Barrio"

import re

reg_str = re.sub('[^a-z0-9]','', test)

print(reg_str)

def remove_lower_case(string:str)->str:
	result = ""
	lower_case = [chr(i) for i in range(ord("a"), ord("z"))]
	for char in test:
		if char in lower_case:
			result += char
	return result

print(remove_lower_case(test))