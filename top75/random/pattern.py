# https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1

'''

n = 3
333222111 times 3
332211 times 2
321 times 1

n = 2
2211 times 2
21 times 1


'''

val = 100
result = sum([i for i in range(0,val+1)])

print((val**2+val)/2)
print(result)