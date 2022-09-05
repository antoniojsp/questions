n = 123433
import math

def invert_integer(number:int)->int:
	result = 0
	while number > 0:
		last_digit= number % 10
		number-=last_digit
		number/=10
		#forming the invert number
		result= result*10 + last_digit

	return int(result)

print(invert_integer(n))





