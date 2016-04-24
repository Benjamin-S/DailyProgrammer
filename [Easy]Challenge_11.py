# The program should take three arguments.
# The first will be a day, the second will be month, 
# and the third will be year. Then, your program should 
# compute the day of the week that date will fall on.
import sys
import math

days = {
	1 : "Sunday",
	2 : "Monday",
	3 : "Tuesday",
	4 : "Wednesday",
	5 : "Thursday",
	6 : "Friday",
	0 : "Saturday"
}

if(len(sys.argv) == 4):
	d = int(sys.argv[1])
	m = int(sys.argv[2])
	Y = sys.argv[3]
	c = int(''.join(Y[0]+Y[1]))
	y = int(''.join(Y[2]+Y[3]))
	y = y-1 if m < 3 else y
	m = m+12 if m < 3 else m

	w = ((d + ((13*(m + 1))/5) + y + (y/4) + (c/4) - 2*c)%7)
	
	print(days[w])
else:
	print("Not enough arguments. Expecting dd mm yyyy.")