# 10. How to find multiple missing numbers in a given integer array with duplicates?


test = [1, 1, 2,2, 3, 5, 5, 7, 9, 9] #length 10 hence max value is 9

def missing_number1(array:list)->list:
	'''
	Values from 1 to N-1 (N is length of the array)
	'''
	current = array[0]
	result = [current]

	for i in range(1,len(array)):
		if result[-1] != array[i]:
			current = array[i]
			if result[-1]+1 != current:
				result.append(0)
			result.append(current)

	return [i+1 for i in range(len(result)) if result[i] == 0]

print(missing_number1(test))


def missing_number(arr:list)->list:
	result = [0]*len(test)
	for i in arr:
		result[i] = 1

	answer = []
	for i in range(1, len(result)):
		if result[i] == 0:
			answer.append(i)


	return answer

print(missing_number(test))





