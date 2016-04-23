#The exercise today asks you to validate a telephone number, 
#as if written on an input form. 
#Telephone numbers can be written as ten digits, or with dashes, 
#spaces, or dots between the three segments, or with the area code 
#parenthesized; both the area code and any white space between 
#segments are optional.
#Thus, all of the following are valid telephone numbers: 
#1234567890, 123-456-7890, 123.456.7890, (123)456-7890, 
#(123) 456-7890 (note the white space following the area code), 
#and 456-7890.
#The following are not valid telephone numbers: 
#123-45-6789, 123:4567890, and 123/456-7890.
phoneNum = raw_input("Please enter a telephone number: ")
patterns = [
	"xxx xxx xxxx", 
	"xxx xxxx", 
	"xxx.xxxx", 
	"(xxx) xxx.xxxx", 
	"(xxx)xxx.xxxx",
	"xxxxxxxxxx",
	"xxx-xxx-xxxx",
	"xxx.xxx.xxxx",
	"(xxx)xxx-xxxx",
	"(xxx) xxx-xxxx",
	"xxx-xxxx"
	]
for num in phoneNum:
	if(num.isdigit()):
		phoneNum = phoneNum.replace(num, 'x')

if(phoneNum in patterns):
	print("Phone Number is Valid. Please proceed.")
else:
	print("Phone Number is Not Valid.")