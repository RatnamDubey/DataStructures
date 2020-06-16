# Linked List Reversal 

## Problem
##Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.
##You are given the example Linked List Node class:
## some_file.py
# from the SIngly Linkled list imported the 
from Implementation_Singly_LinkedList import Singly_Link_list

### Reversal of the linked list 

class Reversal():
     def reverse(self,s):
         prev = None
         current = s.head 
         while current is not None:
             ## This problem can be solved with three pointers 
             # First set Prev pointer , current pointer to head 
             # also set Next pointer to head.next 
             next = current.next 
             # set the head.next pointer to the prev node 
             current.next = prev 
             # move prev node pointer to current node
             prev = current
             # and current to next 
             current = next 

             ## Visual View 
             # https://www.geeksforgeeks.org/reverse-a-linked-list/
             
         s.head = prev     

     def view_list(s):
         a =[]
         while s.head != None:
            a.append(s.head.value)
            s.head = s.head.next
         return(a)


s = Singly_Link_list()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
k = Reversal()
k.reverse(s)
print(s.view_list())