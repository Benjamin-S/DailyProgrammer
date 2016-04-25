#[Easy]Challenge_13.py
'''Find the number of the year for the given date. 
For example, january 1st would be 1, and december 31st 
is 365.
for extra credit, allow it to calculate leap years, 
as well.
'''
# Ugly code :(
import sys
mnth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def dayNum(day, month, leap):
	if month == 1:
		return day
	elif leap == 'y':
		if(month == 2 and day <= 28):
			return((sum(mnth[:month-1])) + day)
		else:
			return((sum(mnth[:month-1])) + day + 1)
	else:
		return((sum(mnth[:month-1])) + day)

day = input("Day(dd): ")
if(day > 31 or day < 1):
	print("Invalid Day Choice. Pick a number between 1 - 31.")
	exit()
month = input("Month(mm): ")
if(month > 12 or month < 1):
	print("Invalid Month Choice. Pick a number between 1 - 12.")
	exit()
leap = raw_input("Is it a leap year? (y or n): ")
if(leap == 'y' or leap == 'n'):
	print(dayNum(day, month, leap))
else:
	print("Invalid choice. Use either y or n.")
	exit()