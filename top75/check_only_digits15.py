# 15. How to check if a string contains only digits?
import re

test1 = "124Antonio"
test2 = "2445"

def check_only_numbers3_regex(string:str)->bool:
	return bool(re.match('[0-9]', string))

print(check_only_numbers3_regex(test1))

def check_only_numbers(string:str)->bool:
	'''
	o(n)
	'''
	for i in string:
		if not i.isnumeric():
			return False

	return True

# print(check_only_numbers(test1))
# print(check_only_numbers(test2))

def check_only_numbers1(string:str)->bool:
	sample = "0123456789"

	for i in string:
		if i not in sample:
			return False

	return True

# print(check_only_numbers1(test1))
# print(check_only_numbers1(test2))




