// You are given an integer array nums and an integer k.

// In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

// Return the maximum number of operations you can perform on the array.

 

// Example 1:

// Input: nums = [1,2,3,4], k = 5
// Output: 2
// Explanation: Starting with nums = [1,2,3,4]:
// - Remove numbers 1 and 4, then nums = [2,3]
// - Remove numbers 2 and 3, then nums = []
// There are no more pairs that sum up to 5, hence a total of 2 operations.
// Example 2:

// Input: nums = [3,1,3,4,3], k = 6
// Output: 1
// Explanation: Starting with nums = [3,1,3,4,3]:
// - Remove the first two 3's, then nums = [1,4,3]
// There are no more pairs that sum up to 6, hence a total of 1 operation.
 

// Constraints:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 109
// 1 <= k <= 109

//My answer (45 out of 51 test cases passed)
class Solution {
    public int maxOperations(int[] nums, int k) {
        int start=0;
        int end=1;
        int ops=0;
        int bool_array[]=new int[nums.length];
        while(start<=nums.length-1)
        {
            if(end<nums.length)
            {
                if(nums[start]+nums[end]==k && bool_array[start]!=1 && bool_array[end]!=1)
                {
                    ops++;
                    bool_array[start]=1;
                    bool_array[end]=1;
                }
                else
                {
                    end++;
                }
                
            }
            else
            {
                start++;
                end=start+1;
            }
        }
        return ops;
    }

}

//The best answer I found in leetcode(Python solution)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans=0
        seen=defaultdict(int)
        for b in nums:
            a=k-b 
            if seen[a]>0:
                ans += 1
                seen[a]-=1
            else:
                seen[b]+=1
        return ans