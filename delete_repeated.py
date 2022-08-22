test = [1,2,3,4,3,3,3,3,4,10,1,1,13,2,3,12,13,2,2,3]

from collections import Counter

class Count:
	def __init__(self, arr):
		self.arr = arr

	def count(self):
		elem_count = {}
		for i in self.arr:
			if i not in elem_count:
				elem_count[i] = 1
			else:
				elem_count[i] +=1
		return elem_count

result = Count(test).count()
print(result.keys())

def delete_repeated(arr:list) -> set:
	already_viewed = set()
	for elem in arr:
		if elem not in already_viewed:
			already_viewed.add(elem)
	return already_viewed

print(delete_repeated(test))



