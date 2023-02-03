"""
Question
Given two non-empty strings, check whether or not they are anagrams. Let us understand anagrams first.

Two strings are anagrams of each other if we can form one string by rearranging the characters of another string.

For instance, 'race' and 'care' are anagrams of each other.

Similarly, 'a net' and 'neat' are anagrams of each other.

Now, create a function that prints

The two strings are anagrams - if the strings are anagrams
The two strings are not anagrams - if the strings are not anagrams
For example,

If the given strings are,

glean
angel
Your program should print The two strings are anagrams.

Assumption: We assume our string will only contain alphabets and a space.
"""

"""
Thought Process
Here, we need to create a function that takes two string parameters.

Since we already know that the passed strings will only contain alphabets and spaces, we can remove spaces from both strings.

After removing the spaces, we also need to sort both strings to compare them with each other.

Now, if both strings are the same, the two strings are anagrams of each other. If they are not the same, the strings are not anagrams.
"""

"""
Challenge:
Check Whether Two Strings are Anagrams
Easy
Problem Description
Create a Python program to check if two strings are anagrams.

Example
Test Input

for the strings 'listen' and 'silent'
Expected Output

The two strings are anagrams
"""
