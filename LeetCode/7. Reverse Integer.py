"""
7. Reverse Integer
Easy
Add to List

Share
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -ç
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
            
        integers = []
        mul = 1

        pow = 10  ** ((len(str(x))-1))
        
        if (len(str(x))) == 0:
            return(0)
        
        if (len(str(x))) == 1:
            return(x)

        elif x * (-1) > 0:
            mul = -1 
            x = x * -1 

        for values in range(len(str(x))):
           val = x%10
           integers.append(val)
           x = int(x/10)

        strings = [str(integer) for integer in integers]
        a_string = "".join(strings)
        an_integer = int(a_string)

        if an_integer > 2147483647:
            return(0)

        else:
            an_integer = an_integer * mul

        return(an_integer)


c = Solution()
print(c.reverse(-1)) 