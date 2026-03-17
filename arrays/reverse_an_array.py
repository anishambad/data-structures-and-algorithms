'''Problem: Reverse an Array (In-Place)

Description:
Given a list of elements, reverse the array in-place without using any extra space
or built-in reverse functions. The goal is to modify the original array so that
the elements appear in reverse order.

Approach:
Use two pointers:
- One pointer (i) starts from the beginning of the array
- Another pointer (j) starts from the end of the array
Swap the elements at these positions and move the pointers towards each other
until they meet.

Time Complexity: O(n)
Space Complexity: O(1) 
'''

def reverse_array(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Reversed array:", reverse_array(arr))
