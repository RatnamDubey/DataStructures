#### Implemented DFS 
#####################

#Algorithm for DFS 

class Deapth_FS():

    def array_init(self , size_arr):
        self.visited = [0]*size_arr 

    def DFS(self , array , start , size_arr):
        if self.visited[start] == 0:
            print(start)
            self.visited[start] = 1 
            for i in range(size_arr):
                if array[start][i] == 1 and self.visited[i] == 0:
                    self.DFS(array,i,size_arr)



###### 
# Creating Adjency Matrix 
asz =  [[0] * 8 for i in range(0,8)]
asz[1][2] = 1 
asz[1][3] = 1 
asz[1][4] = 1 
asz[2][1] = 1 
asz[2][3] = 1 
asz[3][1] = 1 
asz[3][2] = 1 
asz[3][4] = 1 
asz[3][5] = 1 
asz[4][1] = 1 
asz[4][3] = 1 
asz[4][5] = 1 
asz[5][3] = 1 
asz[5][4] = 1 
asz[5][6] = 1 
asz[5][7] = 1 
asz[6][5] = 1 
asz[7][5] = 1 


c = Deapth_FS()
size = 8 
c.array_init(size)
c.DFS(asz,3,size)