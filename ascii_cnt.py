"""
Question
Given a non-empty string, find the total number of capital letters in the string.

If the string does not contain capital letters, print There are no capital letters.

Suppose you are given a string 'The Sun emits UV light'. Here, the total number of capital letters is 4.

Similarly, for the string 'Bread and Butter', the total number of capital letters is 2.
"""
"""
Thought Process
To solve this problem, we need a basic idea of ASCII values.

Of course, we could also make a list of capital letters. And by looping through each character in the given string, we can check if the character is in our created list of capital letters.

But, that is a lot of manual work. Instead, we can check if the ASCII value of the character is between 65 and 90 to know if that character is capital or not.

In Python, we can use the ord() function to get the ASCII value of any string.

ASCII Values

A - 65
B - 66
C - 67
.
.
.
Z - 90
Now, let's look at the steps required to solve this problem:

Define a counter variable with a value of 0.
Loop through each character in the given string.
Check if the character's ASCII value is between 65 and 90.
If the ASCII value of a character is between 65 and 90, that character is a capital letter.
Increment the character by 1.
If the ASCII value of the character is anything else, we can continue the loop.
"""
"""
Challenge:
The Number of Capital Letters in the String
Easy
Problem Description
Create a Python program to count the number of capital letters in a string.

Example
Test Input

For the string 'The Sun emits UV light'
Expected Output

4
"""
# define a function that counts the capital letters in a string
def count_capitals(string):

    # initialize a counter
    capital_counter = 0

    # loop through the string
    for char in string:

        # take the ASCII value of the character and
        # check if it is a capital letter
        if ord(char) >= 65 and ord(char) <= 90:
            capital_counter += 1

    # print the counter
    print(capital_counter)


# call the function
count_capitals('The Sun emits UV light')
