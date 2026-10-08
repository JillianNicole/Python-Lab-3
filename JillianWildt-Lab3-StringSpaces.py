# Function that removes all spaces from a phrase
def stripSpaces(myString):
    newString = ""
    for char in myString:
        if char != " ":
            newString += char
    return newString


# Ask the user for a phrase
phrase = input("Enter a phrase: ")

# Call the function and print the result
result = stripSpaces(phrase)
print("Phrase without spaces:", result)