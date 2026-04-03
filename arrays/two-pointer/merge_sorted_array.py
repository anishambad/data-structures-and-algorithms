"""
Problem: Merge Sorted Array

Description:
You are given two sorted arrays arr1 and arr2, and two integers m and n 
representing the number of valid elements in each array.
Merge arr2 into arr1 as one sorted array in-place.
Note: arr1 has enough space (size m + n) to hold additional elements.

Approach:
Use three pointers starting from the end:
- i for arr1 (last valid element)
- j for arr2
- k for final position in arr1
Place the larger element at position k and move backwards.

Example:
Input: arr1 = [1,2,3,0,0,0], m = 3
       arr2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: Merge both arrays while maintaining sorted order.

"""

def merge_sorted_array(arr1, m, arr2, n):

    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:

        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1

        k -= 1

    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

    return arr1
