### Implemenatation of the Binary Search Tree with the Creation of the Binary search tree 
### Insert elemnent 
### delete element 

### BST has two imp prpperties 
### No duplicates 
## Inorder traversal will give the sorted array 

import queue

class node():
    def __init__(self,val):
        self.data = val
        self.lchild = None 
        self.rchild = None 

    
class Binary_search_tree():

    def insert_bst(self):
        print("Enter the root node")
        var = int(50)
        list01 = [25,75,13,35,60,85,5,20,30,40,55,70,80,95,1,7,6,15,22] 
        if (var != -1):
            root_node = node(var)  
            while list01:
                p = root_node
                q = None 
                print("Enter the child node")
                var2 = list01.pop(0)
                print(var2)
                if var2 == var:
                    print("Root and child node cannot be same ; exiting")
                    break
                elif var2 != -1 :
                    while p is not None:
                        if p.data > var2:
                            q = p
                            p = p.lchild
                        elif p.data < var2:
                            q = p 
                            p = p.rchild

                    if q.data > var2:
                        q.lchild = node(var2)
                    else:
                        q.rchild = node(var2)

                else:
                    break
        return(root_node)

#### Delete Node from the BST 

    def delete_node(self, root_node ,val):
        trav_node = root_node
        q = None
        p = None
        r = None
        if trav_node.data == val:
            trav_node = trav_node.lchild
            while trav_node is not None:
                q = p 
                p = trav_node
                trav_node = trav_node.rchild
            
            root_node.data = p.data
            q.rchild = p.lchild

        else:
            while not trav_node.data == val:
                q = trav_node
                if trav_node.data < val:
                    trav_node = trav_node.rchild
                elif trav_node.data > val:
                    trav_node = trav_node.lchild
            
            if trav_node.lchild is None and trav_node.rchild is None:
                if q.data < val:
                    q.lchild = None
                else:
                    q.rchild = None 
                q.lchild = None 

            elif trav_node.lchild is None and trav_node.rchild is not None:
                print(trav_node.data)
                trav_node = trav_node.rchild
                trav_node.rchild = None 
                q.rchild = trav_node

            elif trav_node.rchild is None and trav_node.lchild is not None:
                print(trav_node.data)
                trav_node = trav_node.lchild
                trav_node.lchild = None 
                q.rchild = trav_node

            elif trav_node.rchild is not None and trav_node.lchild is not None:
                q = trav_node
                trav_node = trav_node.lchild
                while trav_node is not None:
                    r = p
                    p = trav_node
                    trav_node = trav_node.rchild
                q.data = p.data 
                r.rchild = p.lchild 

        return (root_node)


### Search Code in the BST 
    def findnode(self, val):
        print("Enter the node to find ?")
        temp =  int(input())
        p = val
        while p is not None:
            if p.data < temp:
                p = p.rchild
            elif p.data > temp:
                p = p.lchild
            elif p.data == temp:
                print("Node found")
                break
            else:
                print("No node found")
                break
        if p is None:
              print("No node found")




class recursive_iter():
    def inorder_trav(self,val):

        if val != None :
            self.inorder_trav(val.lchild)
            print(val.data)
            self.inorder_trav(val.rchild)




c = Binary_search_tree()
i = recursive_iter()
root = c.insert_bst()
print("Before Deletion")
i.inorder_trav(root)
#c.findnode(root)
upd = c.delete_node(root, 75)
print("After Deletion")
i.inorder_trav(upd)






