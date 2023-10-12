# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
#My answer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

#The best answer I found in Leetcode
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start=len(s)-1
        last=""
        while start>=0:
            if s[start]==" ":
                if len(last)>0:
                    return len(last)
            else:
                last+=s[start]
            start=start-1
        return len(last)