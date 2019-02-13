# Author: Ashley Johnson
# Program: camelCase


def camel_case(sentence):

    wordList = sentence.split()

    # declare and empty string to create the new camel-cased sentence
    new_sentence = ""
    # get the range of the list for the loop iterator
    listLength = len(wordList)

    # use a for loop with an iteration counter. Use this counter variable to reference the index of each word
    # de-case all characters to start, if index is 0 do not capitalize, else all trailing words
    # to be capitalized, then finally concatenate the words together.
    for i in range(listLength):
        word = wordList[i].lower()
        if i == 0:
            new_sentence = new_sentence + word
        else:
            new_sentence = new_sentence + word.capitalize()

    return new_sentence


def main():
    # instructions for user
    print("Enter a sentence to be converted to a camel case variable")
    print("It should not contain any numbers or special characters")
    print('')

    # get a sentence via user input and assign to a variable
    asentence = input("Enter a sentence: ")

    camel_sentence = camel_case(asentence)

    # split the sentence into a list of words to handle each word separately

    print("Your sentence in camel case is: " + camel_sentence)


if __name__ == '__main__':
    main()
