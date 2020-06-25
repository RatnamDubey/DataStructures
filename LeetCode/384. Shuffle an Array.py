"""
Medium

504

1021

Add to List

Share
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
import array
import copy
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.init_nums =  nums
        self.orig = copy.deepcopy(self.init_nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.init_nums = copy.deepcopy(self.orig)
        return(self.init_nums)
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        new_list = [] 
        while True:
            if len(self.init_nums) == 0 :
                pass
                break
            else:  
                while self.init_nums is not None: 
                    if len(self.init_nums) is 0:   
                            break
                    else :
                        ks = random.choice(self.init_nums)  
                        new_list.append(ks)
                        self.init_nums.remove(ks)

                if self.orig == new_list:
                    continue
                else:
                    print(new_list)
                    break  
        self.init_nums = new_list
        return(new_list)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()