# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

#My Answer
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in ransomNote:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in magazine:
            if i in d:
                d[i]-=1
        for i in d.values():
            if i>0:
                return False
        return True

#The best answer I found in Leetcode
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in ransomNote:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in magazine:
            if i in d:
                d[i]-=1
        for i in d.values():
            if i>0:
                return False
        return True