# Implementation of the Converstion of the max heap to the min heap


 ### EDucative Coding Excersise test 1 
 
 
 
 
 
class heap_converstion():
    

    def __init__(self):
        self.heap =[]
        
    def min_heap_converstion(self,values):

        if len(self.heap) == 0 :
            self.heap.append(values)
        
        else:
            self.heap.append(values)
            ## Taking the last values and index 
            index = len(self.heap)-1
            ## Calculating the parent 
            if index%2 == 0 :
                parent = index //2 -1 
            else:
                parent = index//2 

            while parent >= 0:
                if self.heap[parent] > self.heap[index]:
                    self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
                    index = parent
                    if index%2 == 0:
                        parent = index//2-1
                    else:
                        parent= index//2 
                else:
                    break
        return self.heap





def main():
        c = heap_converstion()
        maxHeap = [9,4,7,1,-2,6,5]
        for values in maxHeap:
            minheap = c.min_heap_converstion(values)
        print(minheap)

if __name__ == "__main__":
    main()
