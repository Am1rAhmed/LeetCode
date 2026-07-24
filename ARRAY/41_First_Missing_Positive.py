# Given an unsorted integer array nums. Return the smallest positive 
# integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and 
# uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


# Simple approach using sorting but time comlexity is O(n log n)
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        missing = 1
        for i in range(len(nums)):
            if nums[i] == missing:
                missing += 1

        return missing

# In this approach time complexity is O (2n)-> O(n) and space complexity is O(1)
# class Solution:
#     def firstMissingPositive(self, nums):
#         n = len(nums)
#         i = 0

#         while i < n:
#             num = nums[i]

#             if 1 <= num <= n and nums[num - 1] != num:
#                 nums[i], nums[num - 1] = nums[num - 1], nums[i]
#             else:
#                 i += 1

#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1

#         return n + 1

S = Solution().firstMissingPositive([3,4,-1,1])
print(S)