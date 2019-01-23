# Author: Ashley Johnson
# Program: camelCase

# instructions for user
print("Enter a sentence to be converted to a camel case variable")
print("It should not contain any numbers or special characters")
print('')

# get a sentence via user input and assign to a variable
sentence = input("Enter a sentence: ")

# split the sentence into a list of words to handle each word separately

wordList = sentence.split()

# declare and empty string to create the new camel-cased sentence
newSentence = ""
# get the range of the list for the loop iterator
listLength = len(wordList)

# use a for loop with an iteration counter. Use this counter variable to reference the index of each word
# de-case all characters to start, if index is 0 do not capitalize, else all trailing words
# to be capitalized, then finally concatenate the words together.
for i in range(listLength):
    word = wordList[i].lower()
    if i == 0:
        newSentence = newSentence + word
    else:
        newSentence = newSentence + word.capitalize()

print("Your sentence in camel case is: " + newSentence)

