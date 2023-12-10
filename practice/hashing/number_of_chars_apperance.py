# Hashing without using map data structure
# Only for small characters

def number_of_chars_appearance(string):
	alphabets = [0] * 26

	for char in string:
		alphabets[ord(char) - ord('a')] += 1

	return alphabets


# Only for all 256 characters

def number_of_allcharacter_appearance(string):
	alphabets = [0] * 256

	for char in string:
		alphabets[ord(char)] += 1

	return alphabets



if __name__ == '__main__':
	string = 'abcdeabcdabcz'

	print(number_of_chars_appearance(string))

	alphabets = number_of_allcharacter_appearance(string)

	print(alphabets)
