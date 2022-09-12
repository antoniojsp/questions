# How to sort an integer array in place using the QuickSort algorithm?

arr = [2,5,1,6,5,5,1,3,2,1,10,9]

#chose pivor: len(arr)/2

pivot = int(len(arr)/2)

part1 = arr[:pivot].copy()
part2 = arr[pivot+1:].copy()

left = []
right = []
for i in range(len(part1)):
	if part1[i] > arr[pivot]:
		right.append(part1[i])
	else:
		left.append(part1[i])

for i in range(len(part1)):
	if part2[i] > arr[pivot]:
		right.append(part2[i])
	else:
		left.append(part2[i])

print(left, right)

