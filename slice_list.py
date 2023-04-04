"""
Question

Given a non-empty list, break the list into chunks that contain 4 elements.

For example,

You are given a list of numbers,

numbers = [2, 3, 6, 7, 3, 5, 7, 8, 9, 2, 20, 24, 16, 17, 23, 19]

Here, we can break numbers into chunks,

[2, 3, 6, 7]
[3, 5, 7, 8]
[9, 2, 20, 24]
[16, 17, 23, 19]

"""

"""
Thought Process

To break the lists into chunks, we need to understand lists and slicing.

First, we need to create an empty list to store chunks. So, it'll be a list of lists.

Now, we need to start the loop from 0 to the length of the list, by stepping 3 elements at a time.

Here, using slicing, we need to take 3 elements and store them in another list. Finally, we need to print the elements in the list.

"""
Challenge:
Break a List Into Chunks
Easy
Problem Description

Create a Python program to break a list into chunks of 4 elements.
Example

Test Input
for the list [2, 3, 6, 7, 3, 5, 7, 8, 9, 2, 20, 24, 16, 17, 23, 19]

Expected Output
[2, 3, 6, 7]
[3, 5, 7, 8]
[9, 2, 20, 24]
[16, 17, 23, 19]
"""
# replace ___ with your code

# define a list and empty list to store chunks
numbers = [2, 3, 6, 7, 3, 5, 7, 8, 9, 2, 20, 24, 16, 17, 23, 19]
chunks = []

# start the loop from 0 to the length of the list,
# by step of 3 each time
for i in range(0, len(numbers), 4):

    # from the list, take the 4 elements starting from i
    chunk = numbers[i : i + 4]

    # append the chunk variable to the chunks list
    chunks.append(chunk)


# print the chunks list
for chunk in chunks:
    print(chunk)
"""
 
