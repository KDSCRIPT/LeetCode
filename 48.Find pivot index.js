//My solution
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  let prefix_sum = 0;
  let suffix_sum = nums.reduce((acc, num) => acc + num, 0) - nums[0];
  for (let i = 0; i < nums.length; i++) {
    if (prefix_sum === suffix_sum) return i;
    prefix_sum += nums[i];
    suffix_sum -= nums[i + 1];
    if (prefix_sum === suffix_sum) return i + 1;
  }
  return -1;
};

//The best answer I found in leetcode
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  let totalSum = nums.reduce((acc, num) => acc + num, 0);
  let leftSum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (leftSum * 2 == totalSum - nums[i]) return i;
    leftSum += nums[i];
  }
  return -1;
};
