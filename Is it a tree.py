#User function Template for python3

class Solution:
    def isTree(self, n, adj):
        visited = [False] * n
        parent = [-1] * n

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    parent[neighbor] = node
                    if dfs(neighbor):
                        return True
                elif parent[node] != neighbor:
                    return True
            return False

        if dfs(0):
            return 0  

        for i in range(n):
            if not visited[i]:
                return 0  

        return 1  


