# Author: Ashley Johnson
# Program: List of Classes

# request user input for the number of classes they are taking
numOfClasses = input("How many classes are you taking?: ")

# declare an empty list to store class names
classList = []

# use a for loop with a range specified by user input of total of classes
# with each interation, request the name of a class, then add it to the list
for i in range(int(numOfClasses)):
    className = input("Enter name of Class: ")
    classList += [className]

# use a for loop to print each object in the class list
for i in classList:
    print(i)