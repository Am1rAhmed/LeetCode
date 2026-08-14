# Given a string s, return the maximum length of a substring 
# such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains 
# at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains 
# at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.


class Solution:
    def maximumLengthSubstring(self, s):
        count = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

            while count[ch] > 2:
                first = s[left]
                left += 1
                count[first] -= 1

            ans = max(ans, right - left + 1)

        return ans

S = Solution().maximumLengthSubstring("aaaa")
print(S)