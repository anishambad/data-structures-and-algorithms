"""
Problem: Find Average of Array Elements

Description:
Given an array of numbers, calculate the average of all elements.

Example:
Input: [100, 200, 300, 400, 1000]
Output: 400

Approach:
1. Traverse the array
2. Calculate the sum of all elements
3. Divide the sum by the number of elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

def avg_of_arr(arr):
    total = 0
    
    for i in range(len(arr)):
        total += arr[i]

    avg = total / len(arr)
    return avg


arr = [100, 200, 300, 400, 1000]

print("Average:", avg_of_arr(arr))
