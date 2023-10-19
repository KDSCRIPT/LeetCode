# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

#My Answer
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n>0:
            log_value=math.log2(n)
            if int(log_value)-log_value==0:
                return True
        return False

#The best Answer I found in leetcode
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not(n & n-1)