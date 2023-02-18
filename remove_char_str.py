"""
Question
Given a non-empty string, detect and remove the duplicate letters from the string.

Duplicate characters are characters that appear more than once in the string.

That means, if we are given a string 'mickky', the new string after removing the duplicate character will be 'micky'.

For example,

If the given string is,

12stars23
your program should print,

12star3

Assumption: We will assume the duplicate letter always exists in the given string.
"""

"""
Thought Process
To remove any duplicate elements in a string, we need to create a variable to hold the unique characters.

Now, by looping through each character in the string, we need to check if the character is already in the variable used to store the unique characters.

If the character is not already in the new string, that means the character is unique and we can concatenate it to the new variable.

If the character is already in the new string, that means the character is a duplicate. So we can skip the character.

Finally, we need to print the new string.
"""

"""
Challenge:
Remove Duplicate Characters in the String
Easy
Problem Description
Create a Python program to remove duplicate characters from a string.

Example
Test Input

for the string '12stars23'
Expected Output

12star3
"""

# define a function to remove duplicate characters from a string
def remove_duplicates(string):

    # create a new_string variable to store strings without duplicate characters
    new_string = ''

    # loop through each character in the string
    for char in string:

        # if the character is not in the new_string variable, add it to the new_string variable
        if char not in new_string:
            new_string += str(char)

    # print the new_string variable
    print(new_string)


# call the function
text1 = '12stars23'
remove_duplicates(text1)
