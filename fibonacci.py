n = 10

def fibonacci_inneficient(value:int)->int:
	first_value = 0
	second_value = 1
	temp = 0
	for i in range(0,value):
		temp = second_value
		second_value = first_value + second_value
		first_value = temp

	return temp

# print(fibonacci_inneficient(n))

def fibonacci_array(value:int)->int:
	if value == 0:
		return 0
	fib = [0,1]
	for i in range(value-1):
		temp = fib[i] + fib[i+1]
		fib.append(temp)

	return fib[-1]

# print(fibonacci_array(n))


def fibonacci_recursive(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(9))

def test(value):
	for i in range(value):
		assert fibonacci_array(i) == fibonacci_inneficient(i) 

test(10000)