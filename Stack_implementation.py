#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 07:04:34 2020

@author: ratnamdubey
"""

### Implementation of STacks


class Stack(object):

    def __init__(self):
        self.a = []

    def get_length(self):
        if len(self.a) == 0:
            return "Length is 0"
        else:
            return len(self.a)

    def emptycheck(self):
        if len(self.a) == 0:
            return True
        else:
            return False

    ## Operations

    def pushitem(self,val):
        self.a.append(val)
        return "Item Inserted", val

    def popitem(self):
        if not self.emptycheck():
            poped_item = self.a.pop()
            return "Item Deleted" , poped_item
        else:
            return "Error List is Empty Nothing to remove"



s = Stack()
s.pushitem(10)









