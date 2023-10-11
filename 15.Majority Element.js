// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: 3
// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2
 

// Constraints:

// n == nums.length
// 1 <= n <= 5 * 104
// -109 <= nums[i] <= 109
 

// Follow-up: Could you solve the problem in linear time and in O(1) space?
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count=1;
    nums.sort(function(a, b){return a - b})
    let maxcount=1;
    let majority=nums[0];
    let idx=0;
    while(idx<nums.length)
    {
        if(count>maxcount)
        {
            maxcount=count;
            majority=nums[idx]
        }
        if(nums[idx]===nums[idx+1])
        {
            count++;
        }
        else
        {
            count=1;
        }  
        idx++;
    }
    return majority;
};

//My answer 
var majorityElement = function(nums) {
   let count=1;
   nums.sort(function(a, b){return a - b})
   let maxcount=1;
   let majority=nums[0];
   let idx=0;
   while(idx<nums.length)
   {
       if(count>maxcount)
       {
           maxcount=count;
           majority=nums[idx]
       }
       if(nums[idx]===nums[idx+1])
       {
           count++;
       }
       else
       {
           count=1;
       }  
       idx++;
   }
   return majority;
};

//The best answer i found in leetcode
var majorityElement = function(nums) {
    let candidate = null;
        let count = 0;

        for (const num of nums) {
            if (count === 0) {
                candidate = num;
                count = 1;
            } else if (candidate === num) {
                count += 1;
            } else {
                count -= 1;
            }
        }

        return candidate;
};