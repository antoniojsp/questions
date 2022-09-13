test = "uno dos tres cuatro cinco seis siete ocho nueve diez"


def reverse_sentence(string:str)->str:
	temp = string.split()
	result = ""
	for i in range(len(temp)):
		result += temp.pop() + " "

	return result


def reverse_array(array:str)->str:
	return [array[i] for i in range(len(array)-1,-1,-1)]

def reverse_sentence1(string:str)->str:
	result = []
	temp = ""
	for i in range(0,len(string)):
		if string[i] != " ":
			temp += string[i]
		else:
			result.append(temp)
			temp = ""

		if i == len(string)-1:
			result.append(temp)

	return " ".join(reverse_array(result))

def reverse_sentence2(string:str)->str:

	string_arr = string.split()

	result = ""

	for i in string_arr:
		result = i + " " + result

	return result


print(reverse_sentence2(test))


