# Given a string s, find the length of the longest substring 
# without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. 
# Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a 
# subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        ans = 0

        for right in range(len(s)):
            for i in range(left, right):
                if s[i] == s[right]:
                    left = i + 1
                    break
            ans = max(ans, right - left + 1)

        return ans

S = Solution().lengthOfLongestSubstring("bbba")
print(S)
        