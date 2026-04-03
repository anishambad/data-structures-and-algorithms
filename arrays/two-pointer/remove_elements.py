"""
Problem: Remove Element

Description:
Given an array nums and a value val, remove all occurrences of val in-place.
Return the number of elements remaining after removal.
The order of elements can be changed.

Approach:
Use two pointers:
- i → position to place next valid element
- j → iterate through array
If nums[j] is not equal to val, place it at nums[i].

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2
Explanation: After removing 3, array becomes [2,2,_,_]
Number of valid elements = 2

Time Complexity:
O(n) → We traverse the array once.

Space Complexity:
O(1) → In-place operation, no extra space used.

"""

def remove_elements(nums, val):

    n = len(nums)
    i = 0
    k = 0

    for j in range(n):

        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
            k += 1

    return k
