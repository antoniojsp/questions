# 12. How to check if two Strings are anagrams of each other?

from collections import Counter


s1 = "anna"
s2 = "nana"

def check_anagram1(string1:str, string2:str)->bool:

	if string1 is None or string2 is None:
		return False
	if len(string1) != len(string2):
		return False
		
	str_list1 = list(string1).sort()
	str_list2 = list(string2).sort()

	return str_list1 == str_list2

print(check_anagram1(s1,s2))


def check_anagram(string1:str, string2:str)->bool:
	if string1 is None or string2 is None:
		return False
	if len(string1) != len(string2):
		return False

	freq1 = Counter(string1)
	freq2 = Counter(string2)

	return freq1 == freq2

print(check_anagram(s1, s2))