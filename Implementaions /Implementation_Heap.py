# #### Implementing the Max Heap 

class maxheap():

    def __init__(self):
        self.heap_list = []

    def parent_find(self,data):
            if data %2 == 0:
                value = data//2-1
            else:
                value = data//2
            return(value)

    def insert_heap(self,val):
        if len(self.heap_list) ==  0:
            self.heap_list.append(val)
            return self.heap_list

        else:
            self.heap_list.append(val)
            temp = self.heap_list[-1]
            heap_len = len(self.heap_list)-1
            parent = self.parent_find(heap_len)

            while parent >= 0:                
                if self.heap_list[heap_len] > self.heap_list[parent]:
                    temp = self.heap_list[heap_len]
                    self.heap_list[heap_len] = self.heap_list[parent]
                    self.heap_list[parent] = temp
                    heap_len = parent
                    parent = self.parent_find(heap_len)
                else:
                    break
        
        self.heap_list[heap_len] = temp
        print(self.heap_list)

                     


        


mh = maxheap()
mh.insert_heap(9)
mh.insert_heap(4)
mh.insert_heap(7)
mh.insert_heap(1)
mh.insert_heap(-2)
mh.insert_heap(6)
mh.insert_heap(5)
mh.insert_heap(8)
mh.insert_heap(80)


