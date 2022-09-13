# 21. How to check if two String is a rotation of each other? (solution)

str1 = "1234567890"
str2 = "4567890123"

def check_rotation(s1:str, s2:str)->bool:
	double_string1 = s1*2
	return True if s2 in double_string1 else False

print(check_rotation(str1,str2))
