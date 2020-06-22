## Implementing the tree traversal method 
# Using two mwthods 
# Iterative and recursive method 


## version
# v1.0 - Traverse tree using recursive method 


from Implementation_Binary_Tree import binaryTree
import queue

## These are the itrative method of traversing which is not good way to implement them 



class recursive_iter():
    def preorder_trav(self,val):
        if val != None :
            print(val.data)
            self.preorder_trav(val.lchild)
            self.preorder_trav(val.rchild)
    def inorder_trav(self,val):
        if val != None :
            self.inorder_trav(val.lchild)
            print(val.data)
            self.inorder_trav(val.rchild)
    def postorder_trav(self,val):
        if val != None :
            self.postorder_trav(val.lchild)
            self.postorder_trav(val.rchild)
            print(val.data)

class iterative_method():
    # algo defination in the word file 
    def preorder_trav(self,val):
        q = queue.LifoQueue()
        q.put(val)
        while not q.empty() :          
            curr = q.get()
            print(curr.data)
            if curr.rchild:
                q.put(curr.rchild)
            if curr.lchild:
                q.put(curr.lchild)         
    # Algo defination inthe word file 
    def inorder_trav(self,val):
       stack = queue.LifoQueue()
       curr = val 
       while not stack.empty() or  curr is not None :
            if curr:
               stack.put(curr)
               curr = curr.lchild
            else:
                curr = stack.get()
                print(curr.data)
                curr = curr.rchild

    def postorder_trav(self,val):
        stack1 = queue.LifoQueue()
        stack2 = queue.LifoQueue()
        curr = val
        stack1.put(curr) 
        while not stack1.empty()  :
            temp = stack1.get()
            stack2.put(temp)
            if temp.lchild is not None :
                stack1.put(temp.lchild)
            if temp.rchild is not None:
                stack1.put(temp.rchild)
        while not stack2.empty():
            temp2 = stack2.get()
            print(temp2.data)
            
           
        


           
       
       
       
       
       
       
       
       
       
       
    






c = iterative_method()
root = binaryTree().insert_tree()
# print("recursive preorder")
#c.preorder_trav(root)
# print("recursive inorder")
# c.inorder_trav(root)
c.postorder_trav(root)
# print("recursive postorder")
# c.postorder_trav(root)



