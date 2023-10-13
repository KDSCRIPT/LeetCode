// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2
// Example 2:

// Input: nums = [1,3,5,6], target = 2
// Output: 1
// Example 3:

// Input: nums = [1,3,5,6], target = 7
// Output: 4
 

// Constraints:

// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums contains distinct values sorted in ascending order.
// -104 <= target <= 104

//My Answer
class Solution {
    static int binarySearch(int nums[],int start,int end,int element,int difference,int idx)
    {
        if(start>end)
        {
            return idx;
        }
        int mid=(start+end)/2;
        if(element>nums[mid])
        {
            int curr_difference=element-nums[mid];
            if(curr_difference<difference)
            {
                difference=curr_difference;
                idx=mid+1;
            }
            return binarySearch(nums,mid+1,end,element,difference,idx);
        }
        else if(element==nums[mid])
        {
            return mid;
        }
        else
        {
            int curr_difference=nums[mid]-element;
            if(curr_difference<difference)
            {
                difference=curr_difference;
                idx=mid;
            }
            return binarySearch(nums,start,mid-1,element,difference,idx);
        }
    }
    public int searchInsert(int[] nums, int target) {
        int start=0;
        int end=nums.length-1;
        if(target<=nums[start])
        {
            return start;
        }
        if(target==nums[end])
        {
            return end;
        }
        if(target>nums[end])
        {
            return end+1;
        }
        return binarySearch(nums,start,end,target,Integer.MAX_VALUE,0);
    }
    
}

//The best answer I found in Leetcode
class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0, high = nums.length-1;
        while(low<=high){
            int mid = (low+high)/2;
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) high = mid-1;
            else low = mid+1;
        }
        return low;
    }
}