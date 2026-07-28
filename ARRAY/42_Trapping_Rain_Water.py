# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, h):
        unit = 0
        left = 0
        right = len(h) - 1
        left_max, right_max = 0, 0

        while left < right:

            if h[left] <= h[right]:

                if h[left] >= left_max:
                    left_max = h[left]
                else:
                    unit += left_max - h[left]

                left += 1

            else:

                if h[right] >= right_max:
                    right_max = h[right]
                else:
                    unit += right_max - h[right]
                right -= 1

        return unit

S = Solution().trap([4,2,0,3,2,5])
print(S)