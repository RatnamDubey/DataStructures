# Implementation of the Binary tree 
# Implement the binary tree using Linked list 


### Versions 
    # v1.0 basic tree creation with insertion properties 



class Node():
     def __init__(self,val):
         self.data = val
         self.lchild = None
         self.rchild = None

class Binarytree():

    def __init__(self):
        self.head = None 
       
    def insert(self, val):
        new_node_val = Node(val) 
        traverse_point = self.head
       
        if self.head is None:
            self.head = new_node_val

        else:
             while traverse_point is not None:
                print(traverse_point)
                if val < traverse_point.data:
                     print(val)
                     traverse_point  = traverse_point.lchild 
                     
                else :
                     traverse_point  =  traverse_point.rchild
                print(traverse_point)    

                
             
             traverse_point = new_node_val
             print(traverse_point.data) #



b = Binarytree()
b.insert(10)
b.insert(9)
print(b.head.lchild)

