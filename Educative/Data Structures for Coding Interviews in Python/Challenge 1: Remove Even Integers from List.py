##########################################
### Remove the Even Integers from the List 
###########################################


class operations_maths():
    
    def remove_even(self,list):

        newlist =[]
        for values in list:
            if values % 2 != 0:
                newlist.append(values) 
        return newlist



c = operations_maths()
l = [10,23,45,89,20,12,13,16.17,10]
print(c.remove_even(l))