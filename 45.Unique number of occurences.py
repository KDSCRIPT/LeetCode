#my answer
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=0
            else:
                d[i]+=1
        return len(d.values())==len(set(d.values()))

#The best answer I found in leetcode
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=0
            else:
                d[i]+=1
        return len(d.values())==len(set(d.values()))
