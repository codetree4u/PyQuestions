"""
Find the majority element from the given list of size n.
The majority element in a list is the element that appears more than n/2 times.
For example,
numbers = [1, 7, 8, 7, 7, 7]
Here, 7 is the majority element in the given list. It's because 7 has occurred 4 times, which is greater than 6 / 2, which is 3.
Assumption: We will assume that the list is non-empty and the majority element is always present in the list.
"""
# Write code here  
numbers = [1, 7, 8, 7, 7, 7]
n = len(numbers)

count=0
majorityElement=0

for index in range(n):
    counter =0 
    for frequency in range(n):
        if(numbers[index] == numbers[frequency]):
            counter += 1
        if(counter > count):
            count = counter
            majorityElement = index
if(count > n//2):
    print(numbers[majorityElement])

"""
Thought Process
There are more than n / 2 instances of the majority element in a list of size n.
In order to find the majority element, we must first find the number of times each element appears in the list. 
A built-in method count() in Python counts the number of occurrences of an element.

list.count(element)

Here's how we can solve this problem:

Create a loop to access each list element.
In each iteration of the loop, use the count() function to count the number of occurrences of each element.
Check if the element count is greater than n // 2.
If true, return the element as the majority element.
"""	
