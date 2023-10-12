# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

#My Answer
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in range(len(s)):
            if(s[i] in d1 and d1[s[i]]!=t[i]) or (t[i] in d2 and d2[t[i]]!=s[i]):
                    return False
            else:
                d1[s[i]]=t[i]
                d2[t[i]]=s[i]
        return True

#The best answer I found in Leetcode
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in range(len(s)):
            if(s[i] in d1 and d1[s[i]]!=t[i]) or (t[i] in d2 and d2[t[i]]!=s[i]):
                    return False
            else:
                d1[s[i]]=t[i]
                d2[t[i]]=s[i]
        return True
