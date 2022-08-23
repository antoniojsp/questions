# Input: str1 = “abcdef”, str2 = “defghia” 
# Output: 4 
# Matching characters are: a, d, e, f

str1 = 'abcde'
str2 = 'defghia'

def count(str):
	temp = {}
	for i in str:
		if i not in temp:
			temp[i] = 1
		else:
			temp[i] += 1
	return temp

class Counter:
	def __init__(self, string):
		self.result = {}
		self.string = string

	def count(self):
		for char in self.string:
			if char not in self.result:
				self.result[char] = 1
			else:
				self.result[char] += 1
		return self.result


def matching(str1:str, str2:str)->list:
	count_str1 = Counter(str1).count()
	count_str2 = Counter(str2).count()

	result = []
	for i in count_str1:
		if i in count_str2:
			result.append(i)

	return result

print(matching(str2, str1))

# #with sets
# new1 = set(str1)
# new2 = set(str2)
# print(new2.symmetric_difference(new1))
# # print(new1, new2)
