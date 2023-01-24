"""
Question
Given a non-empty string, find the total number of vowels and consonants present in the string.

In the English alphabet, 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' are vowels and the remaining alphabets are consonants.

Idea Emoji
Assumption: We will assume that given strings only contain alphabets and spaces.
Let's consider you are given the string 'Computer'.

Here, the total number of vowels is 3. And the total number of consonants is 5.

Similarly, for an

Input String: 'juice'

Expected output:

Vowels: 3

Consonants: 2
"""

"""
Thought Process
To count the number of vowels and consonants, we need to define a function that takes a string as a parameter.

First, we need to define a variable named vowels with all possible vowel letters. Then, we need to initialize two counters:

vowel_count - variable to count the number of vowels
consonant_count - variable to count the number of consonants
Now, we need to loop through each character in the string so that we can check each character individually.

If the character is in the vowels string, we have to increment the vowel counter.

Since our sentence can also contain white spaces, we skip the iteration using continue if we encounter a white space.

If none of the above conditions are satisfied, we have to increment the consonant counter.

Finally, we need to print vowel_count and consonant_count .


"""

"""
Challenge:
Number of Vowels and Consonants
Easy
Problem Description
Create a Python program to count the number of vowels and consonants in a string.

Example
Test Input

For the string 'A quick brown fox jumps over the lazy dog'
Expected Output

Vowels: 11
Consonants: 22


"""
