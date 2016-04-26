# Hello, coders! An important part of programming is being able to apply your programs,
# so your challenge for today is to create a calculator application that has use in your life.
# It might be an interest calculator, or it might be something that you can use in the classroom.
# For example, if you were in physics class, you might want to make a F = M * A calc.

# EXTRA CREDIT: make the calculator have multiple functions! 
# Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!
import math

pi = 3.141592654

print("This program will give you different parts of a circle based on the information you have.")
print("What kind of information do you currently have?")
print("1. Diameter")
print("2. Circumference")
print("3. Radius")
print("4. Area")

selection = input("\nInsert corresponding number: ")

def Circ():
	circumference = input("What circumference do you have? ")
	diameter = circumference/pi
	radius = diameter/2
	area = radius*radius*pi
	PrintOut(area, radius, diameter, circumference)

def Rad():
	radius = input("What radius do you have? ")
	diameter = radius*2
	area = radius*radius*pi
	circumference = diameter*pi
	PrintOut(area, radius, diameter, circumference)

def Diam():
	diameter = input("What diameter do you have? ")
	radius = diameter/2
	area = radius*radius*pi
	circumference = diameter*pi
	PrintOut(area, radius, diameter, circumference)

def Area():
	area = input("What area do you have? ")
	radius = math.sqrt(area/pi)
	diameter = radius*2
	circumference = diameter*pi
	PrintOut(area, radius, diameter, circumference)

def PrintOut(area, radius, diameter, circumference):
	print("Circumference: {}".format(round(circumference, 2)))
	print("Radius: {}".format(round(radius, 2)))
	print("Diameter: {}".format(round(diameter, 2)))
	print("Area: {}".format(round(area, 2)))

if selection == 1:
	Diam()
elif selection == 2:
	Circ()
elif selection == 3:
	Rad()
elif selection == 4:
	Area()
else:
	print("Invalid option. Terminating.")
	exit()
