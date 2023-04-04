"""
Challenge:
Sum of Odd Factors
Easy
Problem Description

Create a Python program to find the sum of odd factors of a given number.
Example

Test Input
for the integer 18

Expected Output
13
"""
"""
Question

Given any number, find the factors of that number. Then, return the sum of odd factors.

For example, if you're given 18,

All the factors of 18 are {1, 2, 3, 6, 9, 18}

And, the odd factors of 18 are {1, 3, 9}

So, the sum of odd factors of 18 = 1 + 3 + 9 = 13

"""
Thought Process

To add the odd factors only, we first need to find all factors of the given number. And from these factors, we can select the odd numbers and then calculate the sum.

Steps to solve the problem,

    Initialize an empty list to store all factors of a number.
    Start loop from 1 to the given number.
    If the iteration number is divisible by the original number, that means the iteration number is a factor of the number.
    Append the factor to the factors list.
    Finally, calculate the sum of the odd elements in the factors list using a loop and an if statement.
"""
# function that sums the odd factors of a number
def odd_factor_sum(number):

    # initialize factors list to store all factors
    factors = []

    # start loop from 1 to number
    for i in range(1,number+1):

        # if the number is divisible by i, add i to the factors list
        if number % i ==0:
            factors.append(i)

    # initialize sum to 0
    sum = 0

    # loop through factors list
    for i in factors:

        # if i is odd, add i to sum
        if i%2 !=0:
            sum += i 

    # print the sum
    print(sum)


# call the function
num = 18
odd_factor_sum(num)

"""
"""
We use a for loop to iterate over all the numbers from 1 to num. 
We check if num is divisible by i.
If condition is satisfied, then we append i to factors.
use a second for loop to iterate odd numbers and add them to variable sum.
Finally we print sum.
"""
