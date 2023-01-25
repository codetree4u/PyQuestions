"""
Question
Write a function that can add any number of parameters and print their sum.

For example, if you call the function with parameters 2 and 3, it should return 5.

Also, if you call the function with parameters 5, 4, 3, 2, and 1, it should return 15.
"""
"""
Thought Process
Let's think of functions with parameters. In Python, a function can accept positional arguments and keyword arguments. The number of arguments must match the number of parameters.

However, we can use the concept of packing and unpacking to accept as many arguments as we want.

In Python, * is used to pack elements in a tuple and pass that as arguments in a function.

So, we can create a function with *args as arguments and we can use args as a normal tuple in our function.

This is what we can do :

Create a function with *args as a parameter.
Create a blank sum variable.
By looping through the args variable, add each element to the sum.
Print the sum.
"""
"""
Challenge:
Add Any Number of Parameters
Easy
Problem Description
Create a Python program to add any number of parameters in a function.

Example
Test Input

for function arguments 1, 2, 3, 4, 5
Expected Output

15
"""

# define a function that can add any number of arguments
def adder(___):

    # initialize the sum variable
    sum = 0

    # loop through the arguments and add them to the sum variable
    for ___:
        ___

    # print the sum
    print(sum)


# call the function
adder(1, 2, 3, 4, 5)
