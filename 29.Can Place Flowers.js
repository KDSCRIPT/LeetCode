// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

// Example 1:

// Input: flowerbed = [1,0,0,0,1], n = 1
// Output: true
// Example 2:

// Input: flowerbed = [1,0,0,0,1], n = 2
// Output: false
 

// Constraints:

// 1 <= flowerbed.length <= 2 * 104
// flowerbed[i] is 0 or 1.
// There are no two adjacent flowers in flowerbed.
// 0 <= n <= flowerbed.length

//My Answer(passed 102 out of 128 cases)
var canPlaceFlowers = function(flowerbed, n) {
    let initial_index=0;
    for(let flower=0;flower<flowerbed.length;flower++)
    {
      if(flowerbed[flower]==1)
      {
          initial_index=flower%2;
          break;
      }
    }
    let count=0;
    for(let i=initial_index;i<flowerbed.length;i=i+2)
    {
        if(flowerbed[i]!=1)
        {
          count++;
        }
        if(count>=n)
        {
          return true;
        }
        
    }
    return false;
};

//The best Answer I found in Leetcode
var canPlaceFlowers = function(flowerbed, n) {
    let count = 0;
    let i = 0;
    while(i<flowerbed.length) 
    {
        if (flowerbed[i]===0) 
        {
            if (i===0||flowerbed[i-1]===0) 
            {
                if (i===flowerbed.length-1||flowerbed[i+1]===0) 
                {
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        i++;
    }
  
    return count >= n;
  };