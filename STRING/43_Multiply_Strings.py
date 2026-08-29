# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert 
# the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                x = i + j + 1
                y = i + j

                total = a * b + res[x]

                res[x] = total % 10
                res[y] += total // 10

        st = 0

        while st < len(res) and res[st] == 0:
            st += 1

        ans = ""

        for i in range(st, len(res)):
            ans += str(res[i])

        return ans


S = Solution().multiply("123", "456")
print(S)