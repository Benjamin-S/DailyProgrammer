#Write a program that can translate Morse code in the format of ...---...
#A space and a slash will be placed between words. ..- / --.-
#For bonus, add the capability of going from a string to Morse code.
#Super-bonus if your program can flash or beep the Morse.
#This is your Morse to translate:

morseCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
writtenSentence = 'this is a written sentence to test morse code'

dictionary = {
	'.-' : 'a',
	'-...' : 'b',
	'-.-.' : 'c',
	'-..' : 'd',
	'.' : 'e',
	'..-.' : 'f',
	'--.' : 'g',
	'....' : 'h',
	'..' : 'i',
	'.---' : 'j',
	'-.-' : 'k',
	'.-..' : 'l',
	'--' : 'm',
	'-.' : 'n',
	'---' : 'o',
	'.--.' : 'p',
	'--.-' : 'q',
	'.-.' : 'r',
	'...' : 's',
	'-' : 't',
	'..-' : 'u',
	'...-' : 'v',
	'.--' : 'w',
	'-..-' : 'x',
	'-.--' : 'y',
	'--..' : 'z'
}

def morseToString(morse):
	output = []
	for word in morse.split(' / '):
		translated = []
		for letter in word.split(' '):
			if letter in dictionary:
				translated.append(dictionary[letter])
		sentence = ''.join(translated)
		output.append(sentence)
	final = ' '.join(output)
	return(final)

def stringToMorse(str):
	str = str.lower()
	output = []
	for word in str.split(' '):
		translated = []
		for letter in word:
			for morse, lett in dictionary.items():
				if lett == letter:
					translated.append(morse)
		sentence = ' '.join(translated)
		output.append(sentence)
	final = ' / '.join(output)
	return(final)

#morseToString(morseCode)
#stringToMorse(writtenSentence)
#print(morseToString(stringToMorse(writtenSentence)))