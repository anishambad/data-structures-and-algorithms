"""
🧠 Problem: Reverse Array of Strings

📝 Description:
Given an array of characters, reverse the array in-place.

Example:
Input: ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

---

💡 Approach: Two Pointers
- Use two pointers:
    i -> start
    j -> end
- Swap elements at i and j
- Move both pointers towards center

---

⏱️ Complexity:
Time: O(n)
Space: O(1)
"""

def reverse_array_of_string(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


arr = ["h", "e", "l", "l", "o"]
print(reverse_array_of_string(arr))
