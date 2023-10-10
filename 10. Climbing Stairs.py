# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

#My answer
class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap={0:1,1:1}
        def recusrion(n):
            if n in hashmap:
                return hashmap[n]
            else:
                hashmap[n-1]=recusrion(n-1)
                hashmap[n-2]=recusrion(n-2)
                return recusrion(n-1)+recusrion(n-2)
        return recusrion(n)

#The best answer I found in Leetcode
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]