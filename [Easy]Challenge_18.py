#Often times in commercials, phone numbers contain letters 
#so that they're easy to remember (e.g. 1-800-VERIZON). 
#Write a program that will convert a phone number that
#contains letters into a phone number with only numbers and 
#the appropriate dash. Click here to learn more about the 
#telephone keypad.
#Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278

import string, sys
table = string.maketrans(string.ascii_letters, '22233344455566677778889999' * 2)
#basic = sys.argv[1].translate(table, '-')
basic = raw_input("Number: ").translate(table, '-')
print '{0}-{1}-{2}-{3}'.format(basic[0], basic[1:4], basic[4:7], basic[7:])

#phNo = raw_input("Phone Number: ")
keypad = {
	1 : 1,
	2 : ("a", "b", "c"),
	3 : ("d", "e", "f"),
	4 : ("g", "h", "i"),
	5 : ("j", "k", "l"),
	6 : ("m", "n", "o"),
	7 : ("p", "q", "r", "s"),
	8 : ("t", "u", "v"),
	9 : ("w", "x", "y", "z") 
}

#print(keypad)
