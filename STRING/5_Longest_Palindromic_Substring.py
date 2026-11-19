# Given a string s, return the longest palindromic 
# substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_s = s[i:j+1]
            
                if sub_s == sub_s[::-1]:
                    if len(sub_s) > len(res):
                        res = sub_s
        return res

S = Solution().longestPalindrome("babad")
print(S)