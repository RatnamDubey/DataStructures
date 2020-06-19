#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class sumoftwo():

    def sum(self,list , target):

        if len(list) is None:
            return(0)
        else:
            for idx, val in enumerate(list):
                #list.remove(val)
                for idx2, val2 in enumerate(list):
                    if idx == idx2:
                        pass
                    elif list[idx] + list[idx2] == target:
                        return([list[idx] , list[idx2]])


s = sumoftwo()
print(s.sum([3,2,4],6))