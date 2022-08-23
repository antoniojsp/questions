test = "aaabbddddccccd"

a = "a"

def count(string:list, element_count) -> int:
	counter = 0
	for chat in string:
		if chat == element_count:
			counter +=1 
	return counter

from collections import Counter
counter_a = Counter(test)
print(counter_a[a])

print(count(test, a))