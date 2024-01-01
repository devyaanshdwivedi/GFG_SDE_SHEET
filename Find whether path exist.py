
class Solution:
    
    #Function to find whether a path exists from the source to destination.
    def is_Possible(self, mat):
       # print(mat)
        temp=[[-1,0],[0,1],[1,0],[0,-1]]
        n=len(mat)
        m=len(mat[0])
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if(mat[i][j]==1):
                    source=[i,j]
                    vis[i][j]=1
                elif(mat[i][j]==2):
                    dest=[i,j]
        q=[source]   
        while(q):
            [row,col]=q.pop(0)
            if([row,col]==dest):
                return 1
            for i,j in temp:
                nrow=row+i
                ncol=col+j
                if(0<=nrow<n and 0<= ncol<m and mat[nrow][ncol]!=0 and vis[nrow][ncol]==0):
                    vis[nrow][ncol]=1
                    q.append([nrow,ncol])
                    
        return 0    
            
                    
                    
                    
                
                    
                    
                
