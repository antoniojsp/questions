from collections import Counter

test = "aaddbajdjdjdkkk"


def first_no_repeat(str):
	result = ""
	test_counter = Counter(str)
	print(test_counter)
	for i in test:
		if test_counter[i] == 1:
			return i

	return ""

print(first_no_repeat(test))