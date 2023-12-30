#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        
        if A[0][0] == 0:
            return -1
            
        q = deque()
        q.append([0,0,0]) # r,c,steps
        
        visited = set()
        visited.add((0,0))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            
            r,c,steps = q.popleft()
            
            if r == X and c == Y:
                return steps
                
            
            for dr,dc in directions:
                r1 = dr + r
                c1 = dc + c
                
                
                if 0<=r1<N and 0<=c1<M and (r1,c1) not in visited and A[r1][c1] == 1:
                    q.append([r1,c1,steps+1])
                    visited.add((r1,c1))
                    
        
        return -1
            
        
        
