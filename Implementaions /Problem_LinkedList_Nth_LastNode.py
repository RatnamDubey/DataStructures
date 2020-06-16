# Linked List Nth to Last Node 

## Problem Statement
### Write a function that takes a head node and an integer value **n** and then returns the nth to last node in the linked list. For example, given:

# from the SIngly Linkled list imported the linked list creator 
from Implementation_Singly_LinkedList import Singly_Link_list

### Method 1 # reverse the linked list and then take the value from the back 
## 

class nth_to_last_node():

    def reverse(self,s):
         prev = None
         current = s.head 
         while current is not None:
             next = current.next 
             current.next = prev 
             prev = current
             current = next 
         s.head = prev     

    def nth_node(self,s,val):
        self.reverse(s)
        current = s.head
        cnt = 0 
        if val == 0: 
            return(s.head.value)
        else:
            while current is not None:
                current = current.next
                cnt = cnt + 1 
                if cnt == val :
                    return(current.value)
                    break

   

  
s = Singly_Link_list()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)
s.insert(70)
s.insert(80)
p = nth_to_last_node()
print(p.nth_node(s,1))

