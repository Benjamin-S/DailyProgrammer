#You're challenge for today is to create a random password generator!
#For extra credit, allow the user to specify the amount of passwords to generate.
#For even more extra credit, allow the user to specify the length of the strings he wants to generate!
import random

number = input("How many passwords would you like generated? -->  ")
length = input("And how many characters long should they be? -->  ")
def passGen(number, length):
	for num in range(0, number):
		passArray = []
		for leng in range(0, length):
			passArray.append(chr(random.randrange(33, 127, 2)))
		print(''.join(passArray))

passGen(number, length)