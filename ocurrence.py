test = "aaabbddddccccd"

a = "a"

count = 0

for i in test:
	if i == a:
		count +=1 
print(count)

from collections import Counter

counter_a = Counter(test)
print(counter_a)
print(counter_a[a])