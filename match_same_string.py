test = "abbcndaa"

dictio = {}

for i in test:
	if i in dictio:
		dictio[i] += 1
	else:
		dictio[i] = 1

for i, j in dictio.items():
	if j == 1:
		print(i)