test = "abcjd3ds22ff.//4"

def count_numbers(string:str):
	count = 0
	for i in string:
		if i.isdigit():
			count +=1			
	return count

print(count_numbers(test))