# Create a program that will ask the users name, age, and reddit username.
# Have it tell them the information back, in the format:
		# Your name is (blank), you are (blank) years old, and your username is (blank)
# For extra credit, have the program log this information in a file to be accessed later.

print("Hello there! Could you please enter your name for me?")
name = raw_input("Name: ")

print("Fantastic! Now if you don't mind telling me your age...")
age = raw_input("Age: ")

print("Sweet! Okay last question. What is your reddit username?")
username = raw_input("Username: ")

print("So let me get this straight....")
output = "Your name is {0}, you are {1} years old, and your username is {2}.".format(name, age, username)
print(output)

## Extra Credit
fileOut = open("Data.txt", 'a')
fileOut.write("{0}\n".format(output))
fileOut.close()