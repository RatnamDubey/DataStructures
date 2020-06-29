"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        while("" in strs) : 
            strs.remove("") 
        
        a =[]
        p =[]
        cnt = 0

        if len(strs) == 0:
            return ''
        
        elif len(strs) == 1:
            return strs[0]

        # if len(set(strs)) == 1:
        #     #print(''.join(strs))
        #     return( ''.join(list(set(strs))))

        while True:
            for values in range(len(strs)):
                k = strs[values][cnt]
                #print("mike",k)
                a.append(k)
            
            if len(list(set(a))) == 1:
                m = ''.join(list(set(a)))
                p.append(m)   
                cnt = cnt + 1
                a =[]

            else:
                break 
        
        
        
        str1 = ''.join(p)
        return(str1)
        
             
            
               
       
                 


        







c = Solution()
print(c.longestCommonPrefix(["","b"]))