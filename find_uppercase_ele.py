"""
Question
Given a string of size n, find the index of all the uppercase/capital letters. Your program should print the list of indexes where the uppercase letters are in a string.

For example,

If the given string is,

'heLLo'
Your program should print,

[2, 3]
Similarly, if the given string is 'yes', your program should print [] (an empty list).
"""
"""
Thought Process
To solve this problem, we need to traverse each letter in a string. We also need to track the index of the letter.

First, we can create an empty list to store all the indexes of the uppercase letters in a string.

Then, we need to check if the letter is uppercase. In Python, there is a string method, isupper() that returns true if the letter is in uppercase.

If the letter is capitalized, we need to append its index to the index list which we created earlier.

Finally, we need to print the list of indexes.
"""
"""
Challenge:
Solution
Easy
Problem Description
Create a Python program to display the indexes of uppercase letters in a string.

Example
Test Input

for a string 'heLLo'
Expected Output

[2, 3]
"""

"""
The enumerate() function takes a collection (e.g. a string) and returns it as an enumerate object. The enumerate() function adds a counter as the key(key) of the enumerate object (char).
"""

# define a function that returns
# index list of uppercase letters in a string
def uppercase_indexes(string):

    # initialize an empty list
    index_list = []

    # loop through the string using enumerate
    # so that we can get the index of the letter and the letter itself
    for index, char in enumerate(string):

        # if the letter is in uppercase, add the index to the list
        if char.isupper():
            index_list.append(index)

    # return the list of indexes
    return index_list


# call the function
indexes = uppercase_indexes('heLLo')
print(indexes)
