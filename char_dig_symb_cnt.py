"""
Question
From a given string, count the number of alphabets, digits, and symbols.

For example,

If the given string is,

Hello123.
the program should return,

Alphabets: 5
Digits: 3
Symbols: 1
Assumption: We will assume that spaces are counted as symbols.
"""
"""
Thought Process
In Python, there are inbuilt string methods such as is_digit() and is_alpha() that helps to check if the element is a digit or an alphabet.

We can solve the problem by following these steps:

Create counters for alphabets, digits, and symbols.
Loop through each character in a string.
By using the is_alpha() method, check if the character is the alphabet.
If the character is the alphabet, increment the alphabet counter by 1.
Again, by using the is_digit() method, check if the character is a digit.
If the character is a digit, increment the digit counter by 1.
If none of the above conditions satisfy, increment the symbol counter by 1.
Finally, print the results of all counters.
"""

"""
Challenge:
Alphabets, Digits, and Symbols
Easy
Problem Description
Create a Python program to count the alphabets, digits, and symbols in a string.

Example
Test Input

for the string 'Hello123.'
Expected Output

Alphabets: 5
Digits: 3
Symbols: 1
"""

# define a function that counts alphabets,
# digits and symbols in a string
def counter(string):

    # initialize the counters
    alphabets = 0
    digits = 0
    symbols = 0

    # loop through the string
    for char in string:

        # check if the character is the alphabet
        # if yes, increment the alphabet counter
        if char.isalpha():
            alphabets += 1

        # check if the character is the digit
        # if yes, increment the digit counter
        elif char.isdigit():
            digits += 1

        # check if the character is the symbol
        # if yes, increment the symbol counter
        else:
            symbols += 1

    # print the results
    print('Alphabets:', alphabets)
    print('Digits:', digits)
    print('Symbols:', symbols)


# call the function
counter('Hello123.')
