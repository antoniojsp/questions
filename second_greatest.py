test = [1,9,2,345,323,111,11,93,23893]


class CustomError(Exception):
	def __init__(self,message):
		self.message = message
		super().__init__(self.message)

def first_second_largest(arr:list)->tuple:

	if len(arr) < 2:
		raise CustomError("Array too small")

	(first_large, second_large) = (test[0], test[1]) if test[0] > test[1] else (test[1], test[0])

	for i in range(2,len(test)):
		if test[i] > first_large:
			second_large = first_large
			first_large = test[i] 
		elif test[i] > second_large:
			second_large =  test[i]

	return (first_large, second_large)

print(first_second_largest(test))



