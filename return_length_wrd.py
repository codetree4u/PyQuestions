"""
Question
Given a non-empty string that stores a sentence, return the length of the last word in that string.

A word is a sequence of characters that does not contain white space. For example, 'water', 'python', etc.

For example,

In the string,

I love Python Programming
The length of the last word Programming is 11.

But, even when a sentence ends with a period,

A red rose grew up out of ice.
The length of the last word is 3 because the period is not counted.

Idea Emoji
Assumption: We will assume the string is made of uppercase, lowercase, period, and space characters.
"""

"""
Thought Process
Here, the provided string can contain lowercase letters, uppercase letters, periods, and empty spaces. But we need to count only the alphabets.

So, we need to split the sentence into list elements by white space. Then, we can get the length of the word at the -1 index.

But we also need to check if that last word contains a period at the end. If it does, we need to decrease the count by one.
"""

"""
Challenge:
Length of the Last Word in a String
Easy
Problem Description
Create a Python program to find the length of the last word in a string.

Example
Test Input

for a string 'I love programming'
Expected Output

11
"""
# function that prints length of last word
def length_of_last_word(sentence):

    # split sentence into words
    words_list = sentence.split()

    # get the length of the last word
    result = len(words_list[-1])

    # if there is punctuation at the end of the sentence, remove it from the result
    if '.' in words_list[-1]:
        result -= words_list

    print(result)


# call the function
length_of_last_word('I love programming')
