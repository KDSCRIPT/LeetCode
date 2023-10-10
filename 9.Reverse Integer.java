// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21
 

// Constraints:

// -231 <= x <= 231 - 1
//My Answer(Failed test case 1037/1045 where x =1534236469)
class Solution {
    public int reverse(int x) 
    {
        int reversedNumber=0;
        int BitMinValue=-1*(int)Math.pow(2,31);
        int BitMaxValue=(int)Math.pow(2,31)-1;
        Boolean isNegative=false;
        if(x<0)
        {
            x=x*-1;
            isNegative=true;
        }
        while(x>=1)
        {
            reversedNumber=reversedNumber*10+x%10;
            x=x/10;
            if(!(reversedNumber>=BitMinValue && reversedNumber<=BitMaxValue))
            {
                return 0;
            }
            
        }
        if(isNegative)
        {
            reversedNumber=reversedNumber*-1;
        }
        return reversedNumber;
    }
}

//The best answer I found on Leetcode
class Solution {
    public int reverse(int x) 
    {
        long reversedNumber=0;
        while(x!=0)
        {
            reversedNumber=reversedNumber*10+x%10;
            x=x/10;
            if(reversedNumber<Integer.MIN_VALUE || reversedNumber>Integer.MAX_VALUE)
            {
                return 0;
            }
            
        }
        return (int)reversedNumber;
    }
}