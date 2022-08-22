a = "antonio"
b = "tonnioa"

from collections import Counter

uno = Counter(list(a))
dos = Counter(list(b))

print(uno == dos)

temp1 = sorted(list(a))
temp2 = sorted(list(b))
print(temp1 == temp2)



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