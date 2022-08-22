a = "antonio"
b = "tonnioa"

from collections import Counter


def anagram(str1:str, str2:str) ->bool:
	count_str1 = Counter(list(str1))
	count_str2 = Counter(list(str2))
	return count_str1 == count_str1

print(anagram(a, b))

def anagram_sort(str1:str, str2:str) ->bool:
	list_str1 = list(str1).sort()
	list_str2 = list(str2).sort()
	return list_str1 == list_str2

print(anagram_list(a,b))




# def count(str):
# 	temp = {}
# 	for i in str:
# 		if i not in temp:
# 			temp[i] = 1
# 		else:
# 			temp[i] += 1
# 	return temp

# uno = count(a)
# dos = count(b)

# print(uno == dos)