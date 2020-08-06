class Graph: 

    def __init__(self, row, col, g): 
        self.ROW =  row
        self.COL = col 
        self.graph = g 
        self.worth = []
        self.count = 0

    def isSafe(self, i, j, visited): 
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j]) 
    
    def DFS(self,i, j, visited):            # prints all vertices in DFS manner from a given source. 
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        stack = [] 
  
        stack.append([i,j])  
  
        while (len(stack)):  
            i,j = stack[-1]  
            stack.pop() 

            if (not visited[i][j]):  
                visited[i][j] = True 
                self.worth[self.count]+=self.graph[i][j]

            for k in range(8):  
                if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):  
                    stack.append([i + rowNbr[k], j + colNbr[k]]) 


    def DFSR(self, i, j, visited): 
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1] 
        
        visited[i][j] = True
        self.worth[self.count]+=self.graph[i][j]
       
        for k in range(8): 
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
                self.DFS(i + rowNbr[k], j + colNbr[k], visited) 

    def countIslands(self): 
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 

        count = 0
        for i in range(self.ROW): 
            for j in range(self.COL): 
                if visited[i][j] == False and self.graph[i][j] != 0: 
                    self.worth.append(0)
                    self.DFS(i, j, visited) 
                    count += 1
                    self.count = count

        return self.worth 


# graph = [[1, 1, 0, 0, 0], 
# 		[0, 1, 0, 0, 1], 
# 		[1, 0, 0, 1, 1], 
# 		[0, 0, 0, 0, 0], 
# 		[1, 0, 1, 0, 1]] 

n,m = input().split()
graph = [[int(x) for x in input().split()] for i in range(int(n))]

# print(graph)
row = len(graph) 
col = len(graph[0]) 

g = Graph(row, col, graph) 

worth = g.countIslands()
worth.sort(reverse = True)
print(worth[0])

