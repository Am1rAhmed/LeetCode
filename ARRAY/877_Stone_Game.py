# Alice and Bob play a game with piles of stones. 
# There are an even number of piles arranged in a row, 
# and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. 
# The total number of stones across all the piles is odd, so there are no ties.

# Alice and Bob take turns, with Alice starting first. 
# Each turn, a player takes the entire pile of stones 
# either from the beginning or from the end of the row. 
# This continues until there are no more piles left, at 
# which point the person with the most stones wins.

# Assuming Alice and Bob play optimally, return true if 
# Alice wins the game, or false if Bob wins.

 

# Example 1:

# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice
# takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], 
# and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a 
# winning move for Alice, so we return true.
# Example 2:

# Input: piles = [3,7,2,3]
# Output: true
 

# Constraints:

# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.


class Solution:
    def stoneGame(self, nums):
        store = {}
        def play(nums, left, right):
            if left == right:
                return nums[left]
                
            if (left, right) in store:
                return store[(left, right)]
            
            pick_left = nums[left] - play(nums, left + 1, right)
            pick_right = nums[right] - play(nums, left, right - 1)

            store[(left, right)] = max(pick_left, pick_right)
            return store[(left, right)]

        return play(nums, 0, len(nums) - 1) >= 0 


S = Solution().stoneGame([7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24])  
print(S) 