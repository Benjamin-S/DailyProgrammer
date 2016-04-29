# -*- coding: utf-8 -*-
# Write a function that takes two strings and removes 
#from the first string any character that appears in the second string.
#For instance, if the first string is “Daily Programmer” and the second
#string is “aeiou ” the result is “DlyPrgrmmr”.
#note: the second string has [space] so the space between 
#"Daily Programmer" is removed

s1 = raw_input("First String: ")
s2 = raw_input("Second String: ")

for x in s2:
	trimmed = s1.replace(x, "")
	s1 = trimmed

print(s1)
		