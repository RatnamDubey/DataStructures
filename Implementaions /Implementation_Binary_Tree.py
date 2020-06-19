# Implementation of the Binary tree 
# Implement the binary tree using Linked list 


### Versions 
    # v1.0 basic tree creation with insertion properties 




class child_node():

    def __init__(self,val):
        self.root  = val 
        self.left = None 
        self.right = None 

    
    
class tree():

    def __init__(self):
        self.head = None
        self.left = None
        self.right = None 
    

    def insert_tree(self,value):
        if self.head is None :
            self.head = value 
        
        while 1:
            if self.head is not None:

                if self.head < value:
                    if self.right is not None:
                        self.right = self.right.right
                    else:
                        self.right = child_node(value)
                        break

                
        







tr = tree()
tr.insert_tree(10)
tr.insert_tree(11)
tr.insert_tree(9)