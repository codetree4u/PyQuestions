"""
Question

Given a string of size n, find any character that has at least one same subsequent character.

If multiple characters have the same subsequent, you can return any one of them.

For example, if the given string is Hello, your program should return the letter l as it has the same subsequent character.

Similarly, if the given string is Yahhoo, your program should return either the letter h or the letter o.

Assumption: We will assume the string contains at least one character with the same subsequent character.
"""

"""
Thought Process

In any string, if two letters are repeated one after another, it is said to have the same subsequent characters.

To solve this problem, we need to loop through each letter in a string by the index. And if a character at one index is the same as the character at the next index, that means the character has the same subsequent character.

We need to follow these steps to solve this problem:

    First, we need to loop from 0 to the length of the string using the range() function with len(string) as a parameter.
    Then, we need to compare the character at the current index, with the character at the next index in a string.
    If they are the same, we need to return the character.
"""

"""
Challenge:
Same Subsequent Characters
Easy
Problem Description

Create a Python program to print the character that repeats itself in a subsequent sequence.
Example

Test Input
for the string 'hello'

Expected Output
l

"""
"""
# define a function that returns the letter
# that has the same subsequent letter
def same_subsequent(string):

    # start loop from 0 to length of the string
    for a in range(len(string) -1):

        # if the letter at the current index of the string is
        # equal to the letter at next index of the string
        if string[a] == string[a +1]:

            # return letter at the current index of string
            return string[a]


# call the function
letter = same_subsequent('hello')
print(letter)
"""
"""
Here, we define a function called same_subsequent that takes in a string as its parameter. We then use a for loop to iterate over the characters in the string, except for the last one.
Inside the for loop, we check if the current character is equal to the next character in the string. If they are equal, we print the current character and return from the function.
Finally, we call the print_repeated_character function with the string "hello" as an example. The character 'l' repeats itself in the string "hello", so the output will be 'l'. 
If there are no repeating characters in the string, the function will not print anything.
"""
