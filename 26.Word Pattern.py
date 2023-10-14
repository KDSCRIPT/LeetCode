# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

#My Answer
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        d1={}
        d2={}
        for i in range(len(pattern)):
            if pattern[i] in d1 and d1[pattern[i]]!=words[i] or words[i] in d2 and d2[words[i]]!=pattern[i]:
                return False
            if pattern[i] not in d1:
                d1[pattern[i]]=words[i]
            if words[i] not in d2:
                d2[words[i]]=pattern[i]            
        return True

#The best Answer I found in LeetCode
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        if len(set(pattern))!=len(set(words)):
            return False
        d={}
        for i in range(len(pattern)):
            if pattern[i] in d and d[pattern[i]]!=words[i]:
                return False
            else:
                d[pattern[i]]=words[i]        
        return True

