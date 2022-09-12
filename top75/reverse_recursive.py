test = "maria la del barrio soy"

def reverse_recursive(string:str, length)->str:

	if length == 0:
		return ""

	return string [length-1] + reverse_recursive(string, length-1)

print(reverse_recursive(test, len(test)))