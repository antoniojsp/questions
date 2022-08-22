test = "AlEgria".lower()
vowel = "aeiou"
v = 0
for i in test:
	if i in vowel:
		print(i)
		v += 1

c = abs(len(test) - v)
print (v, c)