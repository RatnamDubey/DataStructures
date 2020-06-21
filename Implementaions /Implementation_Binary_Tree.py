# Implementation of the Binary tree 
# Implement the binary tree using Linked list 

## Abdul bari's playlist 
### Insert the binarty tree using queue method 
### How algo works 
# - Create a root node 
# - put that root node in a quere ; 
# - remove from queue ; check if lefdt or right is null ; if null insert and add to queue 
# - if n othing to add then simply put the child a none 

### Versions 
    # v1.0 basic tree creation with insertion properties 


## import 
import queue



class Node():
     def __init__(self,val):
         self.data = val
         self.lchild = None
         self.rchild = None


class binaryTree():

    def insert_tree(self):
        q = queue.Queue()
        var =  print("Enter the root node")
        var = int(input())
        root_node = Node(var)
        q.put(root_node)
        while not q.empty():
            p = q.get()
            print("Enter the left child")
            var2 = int(input()) 
            if (var2 != -1):
                child_node = Node(var2)
                q.put(child_node)
                p.lchild = child_node            

            print("Enter the right child")
            var3 = int(input()) 
            if (var3 != -1):
                child_node = Node(var3)
                q.put(child_node)
                p.rchild = child_node

        return root_node 

c = binaryTree()
c.insert_tree()