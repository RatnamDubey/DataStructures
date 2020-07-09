##########
#Challenge 2: Find k smallest elements in a List
#Given a list and a number "k" write a function that returns the first "k" smallest elements using a Heap?
##########

class sorted_elements():
    
    def __init__(self):
        self.heap = []
        self.remove_sotr  = []

    def min_heap(self,value):

        if len(self.heap) == 0:
            self.heap.append(value)
        else:
            self.heap.append(value)
            index = len(self.heap) -1 

            if index%2 ==0 :
                parent = index//2 -1 
            else:
                parent = index //2 

            while parent >= 0 :

                if self.heap[index] < self.heap[parent]:
                    self.heap[index] , self.heap[parent] = self.heap[parent] ,self.heap[index]
                    index = parent
                    
                    if index%2 == 0 :
                        parent = index//2-1
                    else:
                        parent = index//2


                else:
                    break
        return(self.heap)
    
    
    def remove_sorted_ele(self,last_index):
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
        self.remove_sotr.append(temp)

        return self.remove_sotr
        





    def k_elements(self,heap_v, k):
        for values in heap_v:
            new_heap = self.min_heap(values)
        print(new_heap)

        for i in range(len(new_heap)-1,-1,-1):
            sorted_heap = self.remove_sorted_ele(i)
        
        print("Min Heap Complete")
        print(sorted_heap)





def main():
        c = sorted_elements()
        maxHeap = [9,4,7,1,-2,6,5]
        c.k_elements(maxHeap ,3)


if __name__ == "__main__":
    main()

