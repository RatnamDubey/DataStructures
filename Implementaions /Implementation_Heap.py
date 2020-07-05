# #### Implementing the Max Heap 

class maxheap():

    def __init__(self):
        self.heap = []


    #### ALgo 
    # Create a max heap 
    # If Heap is empty 
    ####

    def create_maxheap(self,value):

        if len(self.heap) == 0 :
            self.heap.append(value)

        else:
            self.heap.append(value)
        #     ## Compare with parent 
            index = len(self.heap) - 1 
            print("element inserted is" , value)
            print("index is", len(self.heap) -1 )

            ### parent 
            if index % 2 == 0 :
                parent = index //2 - 1
            else:
                parent = (index // 2) 

            while parent >= 0:

                if self.heap[index] > self.heap[parent]:
                    self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
                    index = parent 
                    if index % 2 == 0 :
                        parent = index //2 - 1
                    else:
                        parent = (index // 2)  
                    
                else:
                    break


    
        print(self.heap)


    def delete_heap(self,last_index):

        temp = self.heap[0]
        self.heap[0] = self.heap[last_index]
        
        k = 0 
        left_child = 2*k +1
        right_child = 2*k + 2 

        while left_child <= last_index-1: 

                if self.heap[left_child] > self.heap[right_child]:
                    if self.heap[left_child] > self.heap[k]:
                        self.heap[k],self.heap[left_child] = self.heap[left_child],self.heap[k]
                    
                    k = left_child
                    left_child = 2*k + 1 
                    right_child = 2*k + 2 



                elif self.heap[left_child] < self.heap[right_child]:
                    if self.heap[right_child] > self.heap[k]:
                        self.heap[k],self.heap[right_child] = self.heap[right_child],self.heap[k]
                    k = right_child
                    left_child = 2*k + 1
                    right_child = 2*k + 2


                else:
                    break
        self.heap[last_index] = temp
        return self.heap
        





# print('current hrap is :',c.heap)


def main():
    c = maxheap()
    c.create_maxheap(5)
    c.create_maxheap(20)
    c.create_maxheap(25)
    c.create_maxheap(6)
    c.create_maxheap(30)
    c.create_maxheap(35)
    c.create_maxheap(40)
    for i in range(len(c.heap)-1,-1,-1):
        print("deleted at index"+str(i),c.delete_heap(i))

if __name__ == "__main__":
    main()









