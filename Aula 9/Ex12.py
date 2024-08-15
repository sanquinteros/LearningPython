from sys import argv

word = argv[1]
reversedWord = word[::-1]
isPalindrome = True
counter = 0

while len(word) != counter:
	if word[counter] != reversedWord[counter]:
		isPalindrome = False
		break
	counter = counter + 1

if isPalindrome:
	print("Palavra é um palindromo")
else:
	print("Palavra não é um palindromo")