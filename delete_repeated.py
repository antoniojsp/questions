test = [1,2,3,4,10,1,1,13,2,3,12,13,2,2,3]
from collections import Counter

review = set()
for i in test:
	if i not in review:
		print(i)
		review.add(i)



