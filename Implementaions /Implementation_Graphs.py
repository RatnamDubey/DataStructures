#### Implementation of the Graphs 
### v1.0 - Adjency matrix to show the graphs with the weights and edges 
#### v1.1 - Linked list connect to the array to show the weights 




class graphs():

    ### Matrix Representation 

    def Adjustanct_matrix(self,matrix_size):
        a = [[0]*matrix_size for i in range(matrix_size)]
        return(a)

    def value_insert(self):
        print("enter the size of the matrix")
        size = int(input())
        
        ### Create a empty matrix 
        matrix =  self.Adjustanct_matrix(size)
        ### 
        val = 0 
        while val != -1:
            print("Enter the x value")
            b = int(input())
            print("Enter the y value")
            c = int(input())
            if b == -1 | c == -1:
                break
            elif b > size | c > size:
                print("Entered dim is out of range")
                break
            else:
                print("Enter the weight")
                d = input()
                matrix[b][c] = d 
                print(matrix)

    #### Linked list representation ### Non weighted 











s = graphs()
s.value_insert()
            


    