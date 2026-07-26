
class Solution:
    def isPowerOfFour(self,n):
        if n <= 0:
            return False
        power = 1
        while power < n:
            power = power  * 4
            
        return power == n