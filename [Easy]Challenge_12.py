#Write a small program that can take a string:
#"hi!"
#and print all the possible permutations of the string:
#"hi!"
#"ih!"
#"!hi"
#"h!i"
#"i!h"
#etc...
#thanks to hewts for this challenge!

import itertools
text = raw_input("Input String: ")
for word in list(itertools.permutations(text)):
	print (''.join(word))