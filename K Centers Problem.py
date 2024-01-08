from typing import List


from typing import List


class Solution:
    def kCenterHelper(self, k, n, result, selected, mat):
        if k == 0:
            # Find the maximum distance of a city from the server.
            maxDist = 0
            for i in range(n):
                minDistServer = float('inf')
                for j in range(len(selected)):
                    minDistServer = min(minDistServer, mat[i][selected[j]])
                maxDist = max(maxDist, minDistServer)
            result[0] = min(result[0], maxDist)
        else:
            prev = selected[-1] if selected else -1
            for i in range(prev + 1, n):
                selected.append(i)
                
                # Recursively find ways of selecting the remaining cities.
                self.kCenterHelper(k - 1, n, result, selected, mat)
                
                # Backtrack to explore possible ways of selection without city 'i'.
                selected.pop()

    def selectKcities(self, n, k, mat):
        selected = []
        result = [float('inf')]
       
        # Recursively try all possible ways of selecting 'K' cities.
        self.kCenterHelper(k, n, result, selected, mat)
        
        return result[0]


