#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def numIslands(self,A):
        m,n = len(A), len(A[0])
        vis = [[0]*n for i in range(m)]
        dirs = [[1,0], [0,1], [0,-1], [-1, 0], [1,1], [1,-1], [-1, 1], [-1,-1]]
        
        def visitIsland(i,j):
            pq = deque([(i,j)])
            while pq:
                x,y = pq.popleft()
                for dx, dy in dirs:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 1 and vis[nx][ny]==0:
                        vis[nx][ny] = 1
                        pq.append((nx,ny))
                        
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and vis[i][j] == 0:
                    vis[i][j] = 1
                    ans += 1
                    visitIsland(i,j)
        return ans
