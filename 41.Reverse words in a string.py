# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
#my solution
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()[::-1]
        s1=""
        for i in range(len(words)-1):
            s1+=words[i]+" "
        s1+=words[len(words)-1]
        return s1

#The best answer I found in leetcode(<y own variation of upvoted answers)
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""   
        
        words=[]
        word=""
        for i,char in enumerate(s):
            if char==" ":
                if word!="":
                    words.append(word)
                    word=""
            else:
                word+=char
                if i==len(s)-1:
                    words.append(word)
        return " ".join(words[::-1])
        