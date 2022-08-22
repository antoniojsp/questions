a = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def find_missing(arr):
	lenght = arr[-1]
	suma_real = sum(a)
	suma_teorica = (lenght*(lenght+1)/2)

	return suma_teorica - suma_real

print(find_missing(a))