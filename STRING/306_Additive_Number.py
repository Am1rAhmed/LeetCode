# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. 
# Except for the first two numbers, each subsequent number in the 
# sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an 
# additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, 
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

# Example 1:

# Input: "112358"
# Output: true
# Explanation: 
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:

# Input: "199100199"
# Output: true
# Explanation: 
# The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
 

# Constraints:

# 1 <= num.length <= 35
# num consists only of digits.


class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):

                a = num[:i]
                b = num[i:j]

                if len(a) > 1 and a[0] == '0':
                    continue

                if len(b) > 1 and b[0] == '0':
                    continue

                x = int(a)
                y = int(b)

                k = j
                count = 2

                while k < n:
                    z = x + y
                    s = str(z)

                    if num[k:k + len(s)] != s:
                        break

                    k += len(s)
                    x = y
                    y = z
                    count += 1

                if k == n and count >= 3:
                    return True

        return False


S = Solution().isAdditiveNumber("123")
print(S)