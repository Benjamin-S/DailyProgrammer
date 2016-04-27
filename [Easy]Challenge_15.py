# Write a program to left or right justify a text file
import textwrap

text = raw_input("Input String: ")
w = input("Input Width: ")

def rightJust(text, w):
	for x in textwrap.wrap(text, w):
		print ("{0:>{width}}".format(x, width=w))

def leftJust(text, w):
	print(textwrap.fill(text, w))

rightJust(text, w)
leftJust(text, w)