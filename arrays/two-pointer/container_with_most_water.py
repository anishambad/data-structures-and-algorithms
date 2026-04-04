# =====================================================
# Problem: Container With Most Water
# -----------------------------------------------------
# Given an array 'height' where each element represents 
# the height of a vertical line at that index, find two 
# lines that together with the x-axis form a container 
# that holds the most water.
#
# Example:
# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Approach:
# - Use two pointers: one at the start, one at the end.
# - Calculate area = min(height[i], height[j]) * (j - i).
# - Update max_area if larger.
# - Move the pointer at the smaller height inward.
# =====================================================

def container_with_most_water(height):
    i = 0
    j = len(height) - 1
    max_area = 0

    while i < j:
        # Calculate area between lines i and j
        area = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, area)

        # Move the pointer at the smaller height inward
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area


# -------------------- DRIVER CODE --------------------
height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(height))  # Expected output: 49
