# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

#My answer(I wasnt able to solve this question,had to use the hint)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s=""
        string1=strs[0]
        string2=strs[len(strs)-1]
        for i in range(len(string1)):
            if string1[i]!=string2[i]:
                break
            s+=string1[i]
        return s

#The best answer I found in leetcode
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s=""
        string1=strs[0]
        string2=strs[len(strs)-1]
        for i in range(len(string1)):
            if string1[i]!=string2[i]:
                break
            s+=string1[i]
        return s