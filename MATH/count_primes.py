# Q. Count Primes.

# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106

# https://leetcode.com/problems/count-primes/description/?envType=problem-list-v2&envId=math

class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        primes = [True] * n   
        primes[0] = primes[1] = False  
        p = 2
        while p * p < n:          
            if primes[p]:        
                for i in range(p*p, n, p):
                    primes[i] = False   
            p += 1
        
        return sum(primes)   

    
S =Solution().countPrimes(10000)
print(S)