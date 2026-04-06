"""
Problem: 3Sum

Description:
Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, j != k and nums[i] + nums[j] + nums[k] == 0.

The solution should not contain duplicate triplets.

Approach:
- Sort the array
- Fix one element and use two pointers (left & right)
- Skip duplicates to avoid repeated triplets

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2], [-1,0,1]]
Explanation: These are the only unique triplets whose sum is zero.

Time Complexity:
O(n^2) → Outer loop + two pointer traversal

Space Complexity:
O(1) → Ignoring output list

"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:

    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):

        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total > 0:
                right -= 1
            else:
                left += 1

    return res
