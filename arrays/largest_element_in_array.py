"""
Problem: Find the Largest Element in an Array

Description:
Given an array of integers, find the largest element present in the array.

Example:
Input:  [4, 6, 2, 1, 88]
Output: Maximum element in array is : 88

Approach:
1. Assume the first element of the array as the maximum.
2. Traverse the array starting from the second element.
3. Compare each element with the current maximum.
4. If the current element is greater, update the maximum.
5. After completing the traversal, print the maximum element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def largest_element(arr):
    maxi = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]

    print(f"Maximum element in array is : {maxi}")


arr = [4, 6, 2, 1, 88]
largest_element(arr)
