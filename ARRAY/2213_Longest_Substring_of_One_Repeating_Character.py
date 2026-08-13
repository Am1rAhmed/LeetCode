# You are given a 0-indexed string s. You are also given a 
# 0-indexed string queryCharacters of length k and a 0-indexed 
# array of integer indices queryIndices of length k, 
# both of which are used to describe k queries.

# The ith query updates the character in s at index queryIndices[i] 
# to the character queryCharacters[i].

# Return an array lengths of length k where lengths[i] is the length 
# of the longest substring of s consisting of only one repeating character 
# after the ith query is performed.

 

# Example 1:

# Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# Output: [3,3,4]
# Explanation: 
# - 1st query updates s = "bbbacc". The longest substring 
# consisting of one repeating character is "bbb" with length 3.
# - 2nd query updates s = "bbbccc". 
#   The longest substring consisting of one repeating 
#   character can be "bbb" or "ccc" with length 3.
# - 3rd query updates s = "bbbbcc". The longest substring 
# consisting of one repeating character is "bbbb" with length 4.
# Thus, we return [3,3,4].
# Example 2:

# Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# Output: [2,3]
# Explanation:
# - 1st query updates s = "abazz". The longest substring 
# consisting of one repeating character is "zz" with length 2.
# - 2nd query updates s = "aaazz". The longest substring 
# consisting of one repeating character is "aaa" with length 3.
# Thus, we return [2,3].
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# k == queryCharacters.length == queryIndices.length
# 1 <= k <= 105
# queryCharacters consists of lowercase English letters.
# 0 <= queryIndices[i] < s.length


# Simple but time limit exceeding in LeetCode
class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        s = list(s)
        ans = []

        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            ch = queryCharacters[i]

            s[idx] = ch

            best = 1
            count = 1

            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    count = 1

                if count > best:
                    best = count

            ans.append(best)

        return ans


# Submitted this but not good for understanding
# class Solution:
#     def longestRepeating(self, s, queryCharacters, queryIndices):
#         n = len(s)

#         tree = [[0, 0, 0, 0, 0, 0] for _ in range(4 * n)]

#         def merge(node):
#             a = tree[node * 2]
#             b = tree[node * 2 + 1]

#             left_char = a[0]
#             right_char = b[1]

#             left_len = a[2]
#             right_len = b[3]

#             best = max(a[4], b[4])

#             if a[1] == b[0]:

#                 best = max(best, a[3] + b[2])

#                 if a[2] == a[5]:
#                     left_len = a[5] + b[2]

#                 if b[3] == b[5]:
#                     right_len = b[5] + a[3]

#             tree[node] = [
#                 left_char,
#                 right_char,
#                 left_len,
#                 right_len,
#                 best,
#                 a[5] + b[5]
#             ]

#         def build(node, l, r):
#             if l == r:
#                 x = ord(s[l]) - ord('a')

#                 tree[node] = [
#                     x,
#                     x,
#                     1, 
#                     1,
#                     1, 
#                     1
#                 ]

#                 return

#             mid = (l + r) // 2

#             build(node * 2, l, mid)
#             build(node * 2 + 1, mid + 1, r)

#             merge(node)

#         def update(node, l, r, idx, ch):
#             if l == r:
#                 x = ord(ch) - ord('a')

#                 tree[node] = [
#                     x,
#                     x,
#                     1,
#                     1,
#                     1,
#                     1
#                 ]

#                 return

#             mid = (l + r) // 2

#             if idx <= mid:
#                 update(node * 2, l, mid, idx, ch)
#             else:
#                 update(node * 2 + 1, mid + 1, r, idx, ch)

#             merge(node)

#         build(1, 0, n - 1)

#         ans = []

#         for i in range(len(queryIndices)):
#             idx = queryIndices[i]
#             ch = queryCharacters[i]

#             update(1, 0, n - 1, idx, ch)

#             ans.append(tree[1][4])

#         return ans


S = Solution().longestRepeating("babacc", "bcb", [1, 3, 3])
print(S)