# Implementation of the Linked list 
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

# Implementing the Singly Link List (v1.0) 
class Singly_Link_list():

    # Creating a Head Node 
    # Head Node is initialiaze as None 
    def __init__(self):
        self.head = None 
       
    def insert(self, val):
        new_node_val = Node(val)  ## a 1

        ### Check if Node is Null 
        ## if null insert on the first position else traverse till end then insert 

        if self.head is None:
            self.head = new_node_val
        else:
            temp_point = self.head
            while temp_point.next != None:
                temp_point = temp_point.next
            temp_point.next = new_node_val

    # Implementing the Singly Link List (v1.1)
    # Insert the Linked list in the middle node

    def append(self,val,position):
        new_val = Node(val)

        if self.head is None:
            self.head = new_val
        else:
            temp_point = self.head 
            temp_position = 0 
            while temp_position != position:
                temp_position = temp_position+1
                temp_point = temp_point.next
            new_val.next = temp_point.next
            temp_point.next = new_val
            

    # Delete operation on the head or tail
    def Delete(self, val):
        
        if val == "Head":
            if (self.head) is None:
                return("Errror Head node is Empty")
            else:
                self.head  = self.head.next
        
        else :
            val = val -1 
            pos = 0 
            temp_point = self.head
            while pos != val:
                temp_point = temp_point.next
                print(self.head.value)
                print(self.head.next.value)
                pos = pos + 1 
            temp_point.next = temp_point.next.next

            
    # Added view Linked List content 
    def view_list(self):
        a =[]
        while self.head != None:
            a.append(self.head.value)
            self.head = self.head.next
        return(a)



# Linked List will perform all the operations that are mentioned above in the versions !! 

s = Singly_Link_list()
s.insert(10)
s.insert(20)
s.insert(50)
s.append(25,1)
s.Delete(2)
s.insert(55)
s.insert(60)
s.insert(65)



print(s.view_list())





