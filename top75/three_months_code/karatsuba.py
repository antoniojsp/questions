result = 5678 * 1234
print(result)

a = 56
b = 78
c = 12
d = 34

step1 = a * c
# print(step1)
step2 = b * d
# print(step2)
step3 = (a+b)*(c+d)
# print(step3)
step4 = step3 - step2 - step1
# print(step4)

first = step1*10000
second = step2
third = step4*100
print(f"{str(first)} + {str(second)} + {str(third)} = {str(first+second+third)}")