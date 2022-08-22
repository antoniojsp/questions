# Input: str1 = “abcdef”, str2 = “defghia” 
# Output: 4 
# Matching characters are: a, d, e, f

str1 = 'abcdef'
str2 = 'defghia'

def count(str):
	temp = {}
	for i in str:
		if i not in temp:
			temp[i] = 1
		else:
			temp[i] += 1
	return temp

a = count(str1)
b = count(str2)

vol = a if len(a) > len(b) else b

for i in b:
	if i in a:
		print(i)

#with sets
new1 = set(str1)
new2 = set(str2)
print(new2.symmetric_difference(new1))
# print(new1, new2)
