# 19. How to find all permutations of String? (solution)


'''

P= n!/(n-r)!
n = total elements to chose
r = numbers of elements for the string

test = "abba"

4*3*2*1/(4-2)! = 24/2 = 12 
'''
test = "abcd" #(a,b)(a,c)(a,d)(b,a)(b,c)(b,d)(c,a)(c,b)(c,d)(d,a)(d,b)(dc))


for i in test:
	for j in test:
			if j != i:
				print(i,j)


