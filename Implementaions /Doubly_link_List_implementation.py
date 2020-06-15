# Implementation of the Doubly Linked list 
# v1.0 
# Functionalities : create a class with the linked list 
 # v1.0   # - Insert Operation : on head and tail 
 # v1.1   # - Insert Operation : on the middle node 
 # v1.2   # - Detele Operation : on head and tail 
 # v.1.2.1 # Added View contents of the Linked List 
 # v1.3   # - Delete Opearation : on the middle node 

class Node():
     def __init__(self,val):
         self.value = val
         self.next = None
         self.prev = None 


class DoublyLinkList():

    def __init__(self):
        self.head = None 
        self.tail = None 

    ## need to add get length function 

    def getlength(self):
        count = 0 
        temp_point = self.head
        while temp_point.next != None:
            temp_point = temp_point.next
            count = count + 1 
        return(count)
        
    def insert(self, val):
        new_node_val = Node(val)  ## a 1
        ### Check if Node is Null 
        ## if null insert on the first position else traverse till end then insert 

        if (self.head is None) & (self.tail is None):
            self.head = new_node_val
            self.tail = new_node_val
        else:
            temp_point = self.head
            while temp_point.next != None:
                temp_point = temp_point.next
            temp_point.next = new_node_val
            new_node_val.prev = temp_point
            self.tail = new_node_val

    def append(self,val, position) :
        cnt = self.getlength()
        if position > cnt:
            print("Error Invald position")
        else:
            new_val = Node(val)
            if self.head is None:
                self.head = new_val
                self.tail = new_val

            else:
                temp_position = 0 
                temp_point = self.head
                while temp_position != position:
                    temp_position = temp_position+1
                    temp_point = temp_point.next
                
                new_val.next = temp_point.next
                temp_point.next.prev = new_val
                temp_point.next = new_val
                new_val.prev = temp_point


    def Delete(self,position):
        cnt = self.getlength()
        if position > cnt:
            print("Error Invald position")
        else:
            temp_position = 0 
            temp_point = self.head
            while temp_position != position:
                temp_position = temp_position+1
                temp_point = temp_point.next
            
            temp_point.next = temp_point.next.next
            temp_point.next.prev = temp_point

    # Added view Linked List content 
    def view_list_frnt(self):
        a =[]
        while self.head != None:
            a.append(self.head.value)
            self.head = self.head.next
        return(a)

    # Added view Linked List content 
    def view_list_back(self):
        a =[]
        while self.tail != None:
            a.append(self.tail.value)
            self.tail = self.tail.prev
        return(a)


# Linked List will perform all the operations that are mentioned above in the versions !! 

s = DoublyLinkList()
s.insert(10)
s.insert(11)
s.insert(12)
s.append(25,1)
s.insert(13)
s.append(5,2)
s.Delete(0)
print(s.view_list_frnt()) # traverse from head to tail 
print(s.view_list_back()) # traverse from tail to head
