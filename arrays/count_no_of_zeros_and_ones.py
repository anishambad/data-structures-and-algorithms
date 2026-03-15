"""
Problem: Count Number of Zeros and Ones in an Array

Description:
Given an array containing different integers, count the number of
0s and 1s present in the array. Ignore all other numbers.

Example:
Input:  [1,0,1,1,0,23,54,1,0,1,0,0,1,1,32]

Output:
Total Ones = 7
Total Zeros = 5

Approach:
1. Initialize two counters: zeros and ones
2. Traverse the array
3. If element == 0 → increment zeros
4. If element == 1 → increment ones
5. Ignore other numbers
6. Print the final counts

Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_no_of_zeros_and_ones(arr):
    zeros = 0
    ones = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] == 1:
            ones += 1
        else:
            continue

    print(f"Total Ones = {ones}")
    print(f"Total Zeros = {zeros}")


arr = [1,0,1,1,0,23,54,1,0,1,0,0,1,1,32]
count_no_of_zeros_and_ones(arr)
