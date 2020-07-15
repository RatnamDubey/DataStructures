### Implement the Hash Technique with the hash function 
#### Implementation of the Hash Chaining Technique 

from array import array 


class Node():

    def __init__(self,val):
        self.node = val
        self.next = None 

class Singly_Link_list():
    # Creating a Head Node 
    # Head Node is initialiaze as None 
    def __init__(self):
        self.head = None 
    

class Hashing():

    global func 
    func = 10

    def __init__(self,size=10):
        self.final_table = [0]*size
        self.table_create(size)
        
    def table_create(self,size):
        self.final_table = [0]*size
        for values in range (0,size):
            self.final_table[values] = Singly_Link_list()
        return(self.final_table)

    def Hash_function(self,val, func):
        index = val % func 
        return(index)

    def check_resize(self):
        leng = len(self.final_table)
        cnh = 0 
        for values in range(0,leng):
            if self.final_table[values].head != None:
                cnh = cnh + 1 
        per = cnh/leng
        return(per)

    def collect_values(self,func):
        new_size  = len(self.final_table)
        new_size = new_size * 2
        sz =[]
        for values in range(0,len(self.final_table)):
            tab = self.final_table[values]
            head_lst = tab.head 
            while head_lst is not None:
                sz.append(head_lst.node)
                head_lst= head_lst.next 
        self.final_table = self.table_create(new_size)
        func = func * 2 
        for values in sz:
            
            self.insert_array(values,func)
        #print("Values completed"  ,len(self.final_table))
        
        
    def insert_array(self,val,func):
        new_node_val = Node(val)
        hash_val = self.Hash_function(val,func)
        head_node = self.final_table[hash_val]
        if head_node.head is None:
            head_node.head = new_node_val
        else:
            temp_point = head_node.head
            while temp_point.next != None:
                temp_point = temp_point.next
            temp_point.next = new_node_val

    def create_array(self,val ):
        ###Check the table size 
        if self.check_resize() > 0.6 :
            print('calling resize')
            global func 
            #func = func * 2
            self.collect_values(func)
        else:
            #global func 
            self.insert_array(val,func)




    def print_values(self): 
        for values in range(0,len(self.final_table)):
            z =[]
            tab = self.final_table[values]
            head_lst = tab.head 
            while head_lst is not None:
                z.append(head_lst.node)
                head_lst= head_lst.next 
            print("Index" , values , "has values" , z)






















s = Hashing()
for values in range(1,200):
    s.create_array(values)
s.print_values()
