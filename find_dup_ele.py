"""
Question
From the list of size n, find the duplicate elements in a list and print those elements.

For example,

my_list = [2, 'python', 5, 7, 'python', 'java', 5]
Here, the duplicate elements are 5 and python.

Assumption: Let's assume there always exists at least one duplicate element in the list.
"""

"""
Thought Process
To find the duplicate elements in a list, we first need to know all the elements present on the list.

Then, if any element is present more than once, we can mark it as a duplicate.

In Python, we can use the count() function to find the number of times an element appears on the list.

However, to use count(), we first need access to all the unique elements of the list.

Here is how we solve the problem:

We first convert the list to a set because a set in Python only includes unique elements. Now we have a set with unique elements.
We then run a loop to access each element of the set and use the count() function to check the number of times that element is present in the original list.
If the count() function returns more than 1 for any element of the set, we mark that element as the duplicate element and store it in a new list.
At the end of the loop, we will get a new list of duplicate elements.
"""

"""
Challenge:
Duplicate Elements in the List
Easy
Problem Description
Create a Python program to print the duplicate elements in a list.

Example
Test Input

for a list [2, 'python', 5, 7, 'python', 'java', 5]
Expected Output

[5, 'python']

"""

# define a list
my_list = [2, 'python', 5, 7, 'python', 'java', 5]

# convert list to set, so that
# unique elements will be selected
my_set = set(my_list)

# empty list to store duplicate elements
repeated_elements = []

# loop through my_set and check if the element
# is occurred more than one time in my_list
for char in my_set:
    if my_list.count(char) > 1:
        repeated_elements.append(char)
# print the duplicate elements
print(repeated_elements)
