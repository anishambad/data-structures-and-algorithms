"""
Problem: Reverse Array of Strings

Description:
Given an array of characters (strings), reverse the array in-place.
You must modify the input array without using extra space.

Approach:
Use two pointers:
- i starting from beginning
- j starting from end
Swap elements and move pointers toward each other.

Example:
Input: arr = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Explanation: Elements are swapped from both ends.

Time Complexity:
O(n) → Traverse half of the array

Space Complexity:
O(1) → In-place reversal, no extra space used

"""

def reverse_array_of_string(arr):

    n = len(arr)
    i = 0
    j = n - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr
