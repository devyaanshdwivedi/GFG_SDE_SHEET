class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        #Code here
        from collections import deque
        
        all_rotten = deque()
        all_good = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    all_rotten.append((i,j))
                elif grid[i][j] == 1:
                    all_good.add((i,j))
        
        if len(all_rotten) == 0:
            return 0
            
        step = 0
        while all_rotten:
            
            max_len = len(all_rotten)
            
            for i in range(max_len):
                curr = all_rotten.popleft()
                angles = [
                    (curr[0] - 1, curr[1]),
                    (curr[0], curr[1] - 1),
                    (curr[0] + 1, curr[1]),
                    (curr[0], curr[1] + 1),
                ]
                
                for angle in angles:
                    if angle in all_good:
                        all_good.remove(angle)
                        all_rotten.append(angle)
                    
            step += 1
        
        if len(all_good) > 0:
            return -1
        
        return step - 1
        
                    