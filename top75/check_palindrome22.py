# 22. How to check if the given String is Palindrome? (solution)


from collections import Counter
test = "na"

def is_palindrome(string:str)->bool:

	for i in range(int(len(string)/2)):
		if string[i] != string[(len(string)-1-i)]:
			return False

	return True

def is_palindrome1(string:str)->bool:

	temp = ""
	i = len(string)-1
	while i >= 0:
		temp += string[i]
		i -= 1

	return string == temp

def is_palindrome3(string:str)->bool:

	i = len(string)-1
	while i >=(len(string)-1)/2:
		if string[i] != string[len(string)-1-i]:
			return False
		i -=1

	return True


print(is_palindrome3(test))


x = "malayalam"
 
w = ""
for i in x:
	w = i + w
print(w)


