#write a program that will allow the user to input digits, and arrange them in numerical order.
#for extra credit, have it also arrange strings in alphabetical order

num = raw_input(">")
output = []
for x in num.lower():
	output.append(x)

print(sorted(output))