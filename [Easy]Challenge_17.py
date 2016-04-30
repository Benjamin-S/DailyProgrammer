#write an application which will print a triangle of stars of 
#user-specified height, with each line having twice as many stars
#as the last. sample output:
#@
#@@
#@@@@
#hint: in many languages, the "+" sign concatenates strings.
#bonus features: print the triangle in reverse, print the 
#triangle right justified
v = "@"

rows = input("Rows: ")
print("Triangle")

for x in range(0, rows):
	print(2**x * v)

print("\nReverse")

for y in range(rows-1, -1, -1):
	print(2**y * v)

print("{0:>80}".format("Right justified"))

for z in range(0, rows):
	print("{0:>80}".format(2**z * v))