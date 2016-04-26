#write a program that will print the song "99 bottles of beer on the wall".
#for extra credit, do not allow the program to print each loop on a new line.

def bottleSong(bottles):
	for x in xrange(bottles,0,-1):
		if x > 2:
			print(" {0} bottles of beer on the wall, {0} bottles of beer. Take one down and pass it around, {1} bottles of beer on the wall.".format(x, x-1)),
		elif x == 2:
			print(" {0} bottles of beer on the wall, {0} bottles of beer. Take one down and pass it around, {1} bottle of beer on the wall.".format(x, x-1)),
		else:
			print(" 1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall."),
			print(" No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

#Made it a function so you can pass whatever number you like in. Pointless function practice.
bottleSong(99)