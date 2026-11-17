# Given two strings s1 and s2, return true if 
# s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's 
# permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


class Solution:
    def checkInclusion(self, s1, s2):
        dic_s1 = {}
        dic_s2 = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            if s1[i] in dic_s1:
                dic_s1[s1[i]] += 1
            else:
                dic_s1[s1[i]] = 1

        left = 0

        for right in range(len(s2)):

            if s2[right] in dic_s2:
                dic_s2[s2[right]] += 1
            else:
                dic_s2[s2[right]] = 1

            if right - left + 1 > len(s1):
                dic_s2[s2[left]] -= 1

                if dic_s2[s2[left]] == 0:
                    del dic_s2[s2[left]]

                left += 1

            if dic_s1 == dic_s2:
                return True

        return False


S = Solution().checkInclusion("ab", "eidbaooo")
print(S)
