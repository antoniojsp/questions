test = "maria"
reverse = "airam"
output = ""

antonio = list(test)
last_element = len(antonio) - 1

for i in range(int(len(antonio)/2)):
	antonio[i], antonio[last_element] = antonio[last_element], antonio[i]
	last_element -= 1
	
final = "".join(antonio)
print(final)
print(final == reverse)




# print(temp)
