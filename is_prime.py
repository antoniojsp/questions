
import math
def is_prime(value)->bool:
	for i in range(2,int(value/2)+1):
		if value % i == 0:
			return False
	return True

def is_prime_sqrt(value)->bool:
	for i in range(2,int(math.sqrt(value))):
		if value % i == 0:
			return False
	return True
val = 3
print(is_prime(val))
print(is_prime_sqrt(val))

for i in range(3,100):
	print(i)
	assert is_prime(i) is not is_prime_sqrt(i)


