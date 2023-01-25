"""
Question
Given a dictionary that contains the name and score of the players as a key-value pair, increment every player's score by 1.

For example,

If the dictionary contains,

{'Cody': 50, 'Jack': 57, 'Seth': 59, 'Roman': 67}
Increment everyone's score by 1. That means, the dictionary after the update will be,

{'Cody': 51, 'Jack': 58, 'Seth': 60, 'Roman': 68}
"""
"""

Thought Process
When a for loop is used in a dictionary, it gives us the key of the pair. Using that key, we can get the value in the dictionary.

Let's look at the steps required to do this.

Loop through the dictionary.
Looping gives us the key in each iteration of loop.
Using that key, we can select the value and increment it by 1.
Finally, print the updated dictionary.
"""
"""
Challenge:
Increase Values in a Dictionary
Easy
Problem Description
Create a Python program to increment the values of a dictionary by 1.

Example
Test Input

for a dictionary {'Cody': 50, 'Jack': 57, 'Seth': 59, 'Roman': 67}
Expected Output

{'Cody': 51, 'Jack': 58, 'Seth': 60, 'Roman': 68}
"""
# function that increments every player's score by 1
def incrementer(dictionary):

    # for loop that iterates through the dictionary
    # and increments the score by 1
    for k,v in dictionary.items():
        dictionary[k] = v +1

    # print the updated dictionary
    print(dictionary)


# define the dictionary
player_scores = {
    'Cody': 50,
    'Jack': 57,
    'Seth': 59,
    'Roman': 67,
}

# call the function
incrementer(player_scores)
