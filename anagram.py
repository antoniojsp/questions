a = "antonio"
b = "tonnioad"

from collections import Counter

uno = Counter(list(a))
dos = Counter(list(b))

print(uno == dos)




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