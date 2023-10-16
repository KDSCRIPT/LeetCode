// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

 

// Example 1:

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]
 

// Constraints:

// 1 <= nums.length <= 104
// -231 <= nums[i] <= 231 - 1
 

// Follow up: Could you minimize the total number of operations done?

//My Answer
class Solution {
    public void moveZeroes(int[] nums) {
        int nonzero_index=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]!=0)
            {
                nums[nonzero_index++]=nums[i];
            }
        }
        int zeroes=nums.length-nonzero_index;
        for(int i=0;i<zeroes;i++)
        {
            nums[nonzero_index++]=0;
        }
    }
}

//The best Answer I found in Leetcode
class Solution {
     public void moveZeroes(int[] nums) {
        int snowBallSize = 0; 
        for (int i=0;i<nums.length;i++){
	        if (nums[i]==0){
                snowBallSize++; 
            }
            else if (snowBallSize > 0) {
	            int t = nums[i];
	            nums[i]=0;
	            nums[i-snowBallSize]=t;
            }
        }
    }
}