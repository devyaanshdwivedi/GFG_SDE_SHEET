#User function Template for python3
directionx = [1, 0, -1, 0 ]
directiony = [0, 1,  0, -1]
dirlist = ["D", "R", "U", "L"]
pathfound = 0

class Solution:
    
    def init(self):
        self.path = ""
        self.pathlist = []
        self.visited = [[1,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]]
        
    
    def findPath(self, m, n):
        self.init()
        # code here right , down, left, up
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []
        
        self.traversemaze(0,0,m,n)
        return self.pathlist
         
        
        
        
    def issafe(self, m, row, col, size):
        if not (0<=row<size and  0<=col<size):
            return False
            
        if m[row][col] == 1 and self.visited[row][col] == 0:
            return True
        else :
            return False
    

    def traversemaze(self, xpos, ypos, matrix, size, path = ""):
        
        if xpos == size -1 and ypos == size-1:
            self.pathlist.append(path)
            return True
            
        for dirx in range(4):
            
            curx = xpos + directionx[dirx]
            cury = ypos + directiony[dirx]
            if self.issafe(matrix, curx, cury,size):
                self.visited[curx][cury] = 1
                if self.traversemaze(curx, cury, matrix, size, path+dirlist[dirx]):
                    global pathfound
                    pathfound +=1
                    
                self.visited[curx][cury] = 0
            
        return False
                    
            
            



