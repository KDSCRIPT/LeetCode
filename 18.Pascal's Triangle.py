# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

#My answer
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(2,numRows+1):
            curr=l[len(l)-1]
            t=[]
            t.append(1)
            for j in range(len(curr)-1):
                t.append(curr[j]+curr[j+1])
            t.append(1)
            l.append(t)
        return l

#The best answer I found in leetcode(I found my solution to be reliable)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(2,numRows+1):
            curr=l[len(l)-1]
            t=[]
            t.append(1)
            for j in range(len(curr)-1):
                t.append(curr[j]+curr[j+1])
            t.append(1)
            l.append(t)
        return l
                