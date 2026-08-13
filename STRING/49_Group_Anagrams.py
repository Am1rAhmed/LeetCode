# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be 
# rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as 
# they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# My solution
class Solution:
    def groupAnagrams(self, strs):
        res = []
        used = []
        sorted_words = []

        for word in strs:
            sorted_words.append(sorted(word))

        for i in range(len(strs)):
            if i in used:
                continue

            group = [strs[i]]
            used.append(i)

            for j in range(i + 1, len(strs)):
                if j in used:
                    continue

                if sorted_words[i] == sorted_words[j]:
                    group.append(strs[j])
                    used.append(j)

            res.append(group)

        return res

# Better solution
# class Solution:
#     def groupAnagrams(self, strs):
#         res = {}

#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             if sorted_word not in res:
#                 res[sorted_word] = []
#             res[sorted_word].append(word)

#         return list(res.values())
    
S = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(S)