from math import sqrt, ceil, floor
import time

test =10

def timer(f):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = f(*args, **kwargs)
		end = time.time()
		# print(end - start)
		return result, end - start

	return wrapper

@timer
def factors(number:int)->list:
	'''
	upper_limit: We check all factor till half of the number since the min factor is 2
	i.e: if number is 100, the biggest factor would be 50 since the smaller factor that complements is 2.
	'''

	result = set()
	# upper_limit = int(number/2)+1
	upper = floor(sqrt(number))

	for factor in range(1, upper+1):
		if number % factor == 0:
			result.add(factor)
			result.add(int(number/factor))

	# temp = [int(number/i) for i in result]

	# for i in temp:
	# 	result.add(i)

	return sorted(result)


@timer
def factors_half(number:int)->list:
	'''
	upper_limit: We check all factor till half of the number since the min factor is 2
	i.e: if number is 100, the biggest factor would be 50 since the smaller factor that complements is 2.
	'''

	if number < 1:
		return []

	if number == 1:
		return [1]

	result = set()
	upper = int(number/2)+1

	for factor in range(1, upper+1):
		if number % factor == 0:
			result.add(factor)
	result.add(number) #append number as factor of itself

	return sorted(list(result))

sq_count = 0
half_count = 0
for i in range(10000):
	half, time_half = factors_half(i)
	square, time_square = factors(i)


	if time_half < time_square:
		half_count += 1
	else:
		sq_count += 1

print(f"square {sq_count} vs half {half_count}")
