"""
Created on Mon Jun  8 07:26:36 2020

@author: ratnamdubey
"""


## Deque Implementation

class Deque(object):

    def __init__(self):
        self.a = []

    def get_length(self):
        if len(self.a) == 0:
            return 0
        else:
            return len(self.a)

    def emptycheck(self):
        if len(self.a) == 0:
            return True
        else:
            return False

    ## Operations

    def pushitem(self,val,pos):
        if pos=="F":
            position = 0 
        elif pos=="L":
            position = self.get_length() 
        else:
            return("Inappropriate Position")
        ## 
        self.a.insert(position, val)
    
        

    def popitem(self,pos):
        if not self.emptycheck():
                if pos=="F":
                    position = 0 
                elif pos=="L":
                    position = self.get_length() -1
                else:
                    return("Inappropriate Position")
                ## 
                poped_item = self.a.pop(position)
                return "Item Deleted" , poped_item
        else:
            return "Error List is Empty Nothing to remove"



s = Deque()
s.pushitem(10,"F")