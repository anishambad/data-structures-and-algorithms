# =====================================================
# Problem: Squares of a Sorted Array
# -----------------------------------------------------
# Given a sorted array of integers (which may include 
# negative numbers), return a new array containing the 
# squares of each number, also sorted in non-decreasing 
# order.
#
# Example:
# Input:  [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
#
# Approach:
# - Use two pointers (i at start, j at end).
# - Compare absolute values of arr[i] and arr[j].
# - Place the larger square at the end of result array.
# - Move pointers inward until processed.
# =====================================================

def squares_of_sorted_array(arr):
    n = len(arr)
    res = [0] * n

    i = 0
    j = n - 1
    k = n - 1

    while i <= j:
        if abs(arr[i]) > abs(arr[j]):
            res[k] = arr[i] * arr[i]
            i += 1
        else:
            res[k] = arr[j] * arr[j]
            j -= 1
        k -= 1

    return res


# -------------------- DRIVER CODE --------------------
arr = [-4, -1, 0, 3, 10]
print(squares_of_sorted_array(arr))
