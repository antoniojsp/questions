test = "maria"
reverse = "airam"


def reverse_str(str):
	list_str = list(test)
	last_element = len(list_str) - 1

	for i in range(int(len(list_str)/2)):
		list_str[i], list_str[last_element] = list_str[last_element], list_str[i]
		last_element -= 1
		
	return "".join(list_str)

print(reverse, reverse_str(test))

print(reverse == reverse_str(test))
