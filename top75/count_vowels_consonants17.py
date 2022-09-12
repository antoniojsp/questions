# 17. How to count a number of vowels and consonants in a given String? (solution)

import re

def count_vc(string:str)->tuple:

	count_vowel = 0
	count_consonant = 0
	pattern_vowel = '[aeoiu]'
	patter_consonant = '[b-df-hj-np-tv-z]'

	for i in string:
		if bool(re.match(pattern_vowel, i)):
			count_vowel+=1
		elif bool(re.match(patter_consonant, i)):
			count_consonant+=1


	return (count_vowel, count_consonant)

print(count_vc("antonio"))
