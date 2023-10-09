# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

#My answer(definitely a terrbile solution 😅)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        divider=10
        digits=[]
        if x<0:
            return False
        while(x>0):
            digits.append(x%divider)
            x=x//divider
        for i in range(len(digits)//2):
            if digits[i]!=digits[len(digits)-i-1]:
                return False
        return True

#The best answer I found in Leetcode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        result=0
        original=x
        if x<0 or x%10==0:
            return False
        while(x>0):
            result=result*10+x%10
            x//=10
            return original==result