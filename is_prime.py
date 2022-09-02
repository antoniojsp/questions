
import math
from math import ceil, floor
def is_prime(value)->bool:

	if value <= 1:
		return False
	for i in range(2,int(value/2)+1):
		if value % i == 0:
			return False
	# print(value)
	return True

def is_prime_sqrt(value)->bool:
	if value <= 1:
		return False
	for i in range(2,floor(math.sqrt(value)+1)):
		if value % i == 0:
			return False
	# print(value)
	return True

val = 4
# print(is_prime(val))
# print(is_prime_sqrt(val))

for i in range(3,1000):
	assert is_prime(i) == is_prime_sqrt(i)


