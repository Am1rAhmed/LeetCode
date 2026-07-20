# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same character, 
# but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "f11", t = "b23"

# Output: false

# Explanation:

# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


# My solution is to create two lists, one for each string, 
# that will store the index of the first occurrence of each character. 
# Then, I will compare the two lists to see if they are equal. 
# If they are equal, then the strings are isomorphic.

# class Solution:
#     def isIsomorphic(self, s, t):
#         temp_ind, temp_s = [], []
#         temp_ind_of_t , temp_tt = [], []

#         for i in range(len(s)):
#             if s[i] in temp_s:
#                 index = temp_s.index(s[i])
#                 temp_ind.append(index)
#                 continue 
#             temp_s.append(s[i])
#             temp_ind.append(i)


#         for i in range(len(t)):
#             if t[i] in temp_tt:
#                 index = temp_tt.index(t[i])
#                 temp_ind_of_t.append(index)
#                 continue 
#             temp_tt.append(t[i])
#             temp_ind_of_t.append(i)

#         return temp_ind == temp_ind_of_t

class Solution:
    def isIsomorphic(self, s, t):
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] in s_map:
                if s_map[s[i]] != t[i]:
                    return False
            else:
                s_map[s[i]] = t[i]

            if t[i] in t_map:
                if t_map[t[i]] != s[i]:
                    return False
            else:
                t_map[t[i]] = s[i]

        return True

S = Solution().isIsomorphic("f11", "b23")
print(S)