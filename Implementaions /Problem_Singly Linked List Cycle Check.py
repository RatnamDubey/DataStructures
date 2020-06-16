# Singly Linked List Cycle Check 

## Problem
# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
# You've been given the Linked List Node class code:

import nose

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

# Actual solution 

def cycle_check(node):
    if node is None :
        print ("Error Node is empty ")
    else:
        temp_var = node.nextnode
        while temp_var != None:
            temp_var = temp_var.nextnode
            if node.nextnode == temp_var.nextnode:
                return(True)
            elif temp_var.nextnode == None:
                return(False)           
        return(False)


# How solution works 
    # traversing the whole linked list 
    # if the first value in the linked list is empty then throws an erro 
    # if that passes then traverse the whole linked list and check if the first head node == last node
    # if that is there "yes" circular 
    # and if we find none in the tail if the list 
    # return False









# Test Part 
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print ("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)


