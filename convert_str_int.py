"""
Question
You are given two numbers but in string format. Now, you need to multiply them and return the multiplication, that too in a string format.

For example, if the given strings are '12' and '10', your program should return '120'.

Assumption: We will assume the string will always contain numbers. The numbers could be positive or negative integers.
"""

"""
Thought Process
We know that although the given data are in string format, they contain numbers. So it should be easy to convert these strings into integers.

In Python, we can convert string data to integers by using the int() function. Let's look at the steps we need to follow to solve this problem.

We need to convert both strings to integers.
Since they are both integers, we can multiply them.
Finally, we need to convert the product to string format.
"""

"""
Challenge: Multiply Strings as Integers
Easy 
Problem Description
Create a Python program to multiply two strings as integers.

Example
Test Input

For the strings '10' and '20'
Expected Output

200
"""

# define a function that takes numeric strings as parameter
# and returns the product of it in string format
def multiply(string1, string2):

    # convert the strings to integers
    num1 = int(string1)
    num2 = int(string2)

    # multiply the numbers
    product = num1 * num2

    # convert the product to string
    string_product = str(product)

    # print the product
    print(string_product)


# call the function
multiply('10', '20')
