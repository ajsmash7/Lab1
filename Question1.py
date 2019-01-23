# Author: Ashley Johnson
# Program: Hello, birthday month

# ask the user to input their name and birthday month
name = input("What is your name?: ")
month = input("What month were you born in?: ")

# use the len function to count the number of characters in name variable, assign it to a new variable
nameCount = len(name)

# convert user entry to all lower case, use an if conditional to test whether month is January
# if true, print Happy Birthday. If false, print that it's not your birthday
if month.lower() == "january":
    print("Happy Birthday Month!")
else:
    print("It is not your birthday month")

# print the number of characters in a name. I used concatenation which required casting the integer to string.
print("There are " + str(nameCount) + " letters in your name")