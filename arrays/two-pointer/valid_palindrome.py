"""
🧠 Problem: Valid Palindrome

📝 Description:
Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

A palindrome reads the same forward and backward.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True

---

💡 Approach: Two Pointers
- Use two pointers:
    i -> start
    j -> end
- Skip non-alphanumeric characters
- Compare characters in lowercase
- If mismatch → return False
- Else → move both pointers

---

⏱️ Complexity:
Time: O(n)
Space: O(1)
"""

def valid_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:

        while i < j and not s[i].isalnum():
            i += 1

        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))
