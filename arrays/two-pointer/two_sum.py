"""
🧠 Problem: Two Sum (Sorted Array)

📝 Description:
Given a sorted array of integers, find two numbers such that they add up to a target.
Return their 1-based indices.

Example:
Input: arr = [1, 2, 3, 5, 6, 7], target = 11
Output: [4, 6]

---

💡 Approach: Two Pointers
- Initialize two pointers:
    i -> start (0)
    j -> end (n-1)
- While i < j:
    - If sum < target → move i forward
    - If sum > target → move j backward
    - If sum == target → return indices

---

⏱️ Complexity:
Time: O(n)
Space: O(1)
"""


def two_sum(arr, target):
    i, j = 0, len(arr) - 1

    while i < j:
        current_sum = arr[i] + arr[j]

        if current_sum < target:
            i += 1
        elif current_sum > target:
            j -= 1
        else:
            return [i + 1, j + 1]

    return [] 


# 🔽 Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 7]
    target = 11
    print(two_sum(arr, target))
