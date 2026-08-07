# You are given a string num which represents a positive integer, and an integer t.

# A number is called zero-free if none of its digits are 0.

# Return a string representing the smallest zero-free 
# number greater than or equal to num such that the product 
# of its digits is divisible by t. If no such number exists, return "-1".

 

# Example 1:

# Input: num = "1234", t = 256

# Output: "1488"

# Explanation:

# The smallest zero-free number that is greater than 1234 
# and has the product of its digits divisible by 256 is 1488,
#  with the product of its digits equal to 256.

# Example 2:

# Input: num = "12355", t = 50

# Output: "12355"

# Explanation:

# 12355 is already zero-free and has the product of its digits 
# divisible by 50, with the product of its digits equal to 150.

# Example 3:

# Input: num = "11111", t = 26

# Output: "-1"

# Explanation:

# No number greater than 11111 has the product of its digits divisible by 26.

 

# Constraints:

# 2 <= num.length <= 2 * 105
# num consists only of digits in the range ['0', '9'].
# num does not contain leading zeros.
# 1 <= t <= 1014

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Factor t into 2^a * 3^b * 5^c * 7^d
        need = [0, 0, 0, 0]

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[i] += 1
                t //= p

        # Any other prime factor can never come from digits 1..9
        if t != 1:
            return "-1"

        # Prime factors supplied by digits 0..9
        fac = [
            (0, 0, 0, 0),  # 0 - unused
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        def sub(req, d):
            f = fac[d]
            return (
                max(0, req[0] - f[0]),
                max(0, req[1] - f[1]),
                max(0, req[2] - f[2]),
                max(0, req[3] - f[3]),
            )

        # Exact minimum number of digits needed to cover req.
        #
        # 5 and 7 each require their own digit.
        # For factors 2 and 3, use the most compact digits:
        # 8 = 2^3, 9 = 3^2, 6 = 2*3, etc.
        def min_len(req):
            a, b, c, d = req

            ans = c + d

            # Handle 2/3 factors.
            #
            # Try the small number of useful ways to use digit 6.
            best = 10**18

            # In an optimal representation, after grouping by 8 and 9,
            # only a tiny interaction between 2 and 3 remains.
            for six in range(3):
                if six > a or six > b:
                    break

                x = a - six
                y = b - six

                cnt = six

                cnt += x // 3
                x %= 3

                cnt += y // 2
                y %= 2

                if x == 2:
                    cnt += 1       # digit 4
                elif x == 1:
                    cnt += 1       # digit 2

                if y == 1:
                    cnt += 1       # digit 3

                best = min(best, cnt)

            return ans + best

        # Build the lexicographically smallest suffix of exactly `length`
        # digits that can satisfy req.
        def make_suffix(req, length):
            out = []

            for pos in range(length):
                left = length - pos - 1

                for d in range(1, 10):
                    nxt = sub(req, d)

                    if min_len(nxt) <= left:
                        out.append(str(d))
                        req = nxt
                        break
                else:
                    return None

            if req == (0, 0, 0, 0):
                return "".join(out)

            return None

        n = len(num)
        initial = tuple(need)

        # prefix_req[i] = remaining requirements after consuming num[:i].
        #
        # This lets us move from right to left without recomputing the
        # whole prefix, avoiding O(n^2).
        prefix_req = [None] * (n + 1)
        prefix_req[0] = initial

        first_zero = n

        for i, ch in enumerate(num):
            if ch == '0':
                first_zero = i
                break

            prefix_req[i + 1] = sub(prefix_req[i], int(ch))

        # If there was no zero, num itself may already work.
        if first_zero == n:
            if prefix_req[n] == (0, 0, 0, 0):
                return num

            start = n - 1

        else:
            # We cannot preserve the zero or anything after it.
            #
            # First try replacing this zero with 1..9 while preserving
            # everything before it.
            i = first_zero
            req = prefix_req[i]
            remaining = n - i - 1

            for d in range(1, 10):
                nxt = sub(req, d)

                if min_len(nxt) <= remaining:
                    suffix = make_suffix(nxt, remaining)

                    if suffix is not None:
                        return num[:i] + str(d) + suffix

            # If that fails, increase an earlier digit.
            start = i - 1

        # Increase the rightmost possible digit.
        #
        # Changing a later position is always better than changing an
        # earlier position because we want the smallest number >= num.
        for i in range(start, -1, -1):
            current = int(num[i])
            req = prefix_req[i]
            remaining = n - i - 1

            for d in range(current + 1, 10):
                nxt = sub(req, d)

                if min_len(nxt) <= remaining:
                    suffix = make_suffix(nxt, remaining)

                    if suffix is not None:
                        return num[:i] + str(d) + suffix

        # No number of the same length works.
        # Build the smallest valid number with more digits.
        length = max(n + 1, min_len(initial))

        suffix = make_suffix(initial, length)

        if suffix is not None:
            return suffix

        return "-1"

S = Solution().smallestNumber("1234", 256)
print(S)