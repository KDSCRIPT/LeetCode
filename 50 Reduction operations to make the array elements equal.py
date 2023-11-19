#I couldnt solve this question(This was a really difficult one)
#The best answer I found in leetcode
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
        res = 0
        operations = 0
        for i in range(max_num, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                res += operations - freq[i]
        return res