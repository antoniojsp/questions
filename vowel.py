
def number_vowel_consonant(string:str)->tuple:
	vowels = "aeiou"
	consonants = "bcdfghjklmnpqrstvwxyz"
	vowel_number = 0
	consonant_number = 0
	for char in string.lower():
		if char in vowels:
			vowel_number += 1
		if char in consonants:
			consonant_number += 1

	return (vowel_number, consonant_number)

test = "AlEgria"		
print(number_vowel_consonant(test))		
