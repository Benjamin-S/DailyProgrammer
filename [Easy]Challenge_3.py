# Write a program that can encrypt texts with an alphabetical caesar cipher.
# This cipher can ignore numbers, symbols, and whitespace.
# for extra credit, add a "decrypt" function to your program!

test = raw_input("Enter: ")
def encrypt(message):
	outWord = []
	for letter in range(len(message)):
		temp = ord(message[letter]) - 1
		outLetter = chr(temp)
		outWord.append(outLetter)
	out = ''.join(outWord)
	return out

def decrypt(message):
	outWord = []
	for letter in range(len(message)):
		temp = ord(message[letter]) + 1
		outLetter = chr(temp)
		outWord.append(outLetter)
	out = ''.join(outWord)
	return out

encryptedText = encrypt(test)
print(encryptedText)
print(decrypt(encryptedText))