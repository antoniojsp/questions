n = 123451234
print(n)
import math

result = 0
count = math.floor(math.log10(n)+1)
while n > 0:
	temp = n % 10
	n =  n - temp
	print(int(temp))
	n = n/10
	result =  result*10 + temp

print(int(result))

# 5 = 0 + 5
# 54 = 50 + 4
# 543  =54+ 3
# 5432 = 543 + 2
# 54321 5432 + 1
		





