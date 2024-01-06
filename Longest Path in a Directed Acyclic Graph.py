from typing import List


from typing import List


class Solution:
    def maximumDistance(self, v : int, e : int, src : int, edges : List[List[int]]) -> List[int]:
        # code here
        # time -- O(v + e)
        # space -- O(v)
        
        # topo order
        def topoOrder(node, visited, adj, order):
            visited[node] = True
            
            for adjel, w in adj[node]:
                if not visited[adjel]:
                    topoOrder(adjel, visited, adj, order)
            
            order.append(node)
            
        
        adj = [[] for i in range(v)]
        
        for a, b, w in edges:
            adj[a].append((b, w))
        
        visited = [False]*v
        
        order = []
        for i in range(v):
            if not visited[i]:
                topoOrder(i, visited, adj, order)
        
        dist = [float("-inf")]*v
        # pop out and relax each node
        
        dist[src] = 0
        while order:
            el = order.pop()
            
            for adjel, w in adj[el]:
                if dist[adjel] < dist[el] + w:
                    dist[adjel] = dist[el] + w
        
        for i in range(v):
            if dist[i] == float("-inf"):
                dist[i] = "INF"
        
        return dist
        
        
                
            
        





#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        v = int(input())
        
        
        e = int(input())
        
        
        src = int(input())
        
        
        edges=IntMatrix().Input(e, e)
        
        obj = Solution()
        res = obj.maximumDistance(v, e, src, edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends

from typing import List


class Solution:
    def maximumDistance(self, v : int, e : int, src : int, edges : List[List[int]]) -> List[int]:
        # code here
        adjList = {}
        for i in range(v):
            adjList[i] = {}
        for i in edges:
            adjList[i[0]][i[1]] = i[2]
        dp = {}
        def dfs(node, dest):
            if node == dest:
                return 0
            key = (node, dest)
            if key in dp:
                return dp[key]
            y1 = -float('inf')
            for i in adjList[node]:
                x = dfs(i, dest)+adjList[node][i]
                y1 = max(x,y1)
            dp[key] = y1
            return dp[key]
        res = []
        for i in range(v):
            #dp = {}
            x = (dfs(src, i))
            if x <= -float('inf'):
                res.append("INF")
            else:
                res.append(x)
        return res
        
                
            
        

