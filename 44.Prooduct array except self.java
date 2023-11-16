// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

 

// Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
// Example 2:

// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]
 

// Constraints:

// 2 <= nums.length <= 105
// -30 <= nums[i] <= 30
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

// Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

//My solution
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefix_product[]=new int[nums.length];
        int suffix_product[]=new int[nums.length];
        int final_array[]=new int[nums.length];
        int prefix_idx=0;
        int suffix_idx=nums.length-1;
        int final_idx=0;
        int curr_prefix_product=1;
        for(int i=0;i<nums.length;i++)
        {
            prefix_product[prefix_idx++]=curr_prefix_product;
            curr_prefix_product*=nums[i];
        }
        int curr_suffix_product=1;
        for(int i=nums.length-1;i>=0;i--)
        {
            suffix_product[suffix_idx--]=curr_suffix_product;
            curr_suffix_product*=nums[i];
        }
        for(int i=0;i<nums.length;i++)
        {
            final_array[final_idx++]=prefix_product[i]*suffix_product[i];
        }
        return final_array;

    }
}

//The best answer I found in leetcode
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int final_array[]=new int[n];
        for(int i=0;i<n;i++)final_array[i]=1;
        int product=1;
        for(int i=0;i<n;i++)
        {
            final_array[i]=product;
            product*=nums[i];
        }
        product=1;
        for(int i=nums.length-1;i>=0;i--)
        {
            final_array[i]*=product;
            product*=nums[i];
        }
        return final_array;
    }
}