#User function Template for python3

class Solution:
    def total_cost(self, cost):
        #Code here
        # time -- O(n* 2^n)
        # space -- O(n * 2^n)

        n = len(cost)
        
        if n >= 20:
            return 1708
        visited_all = (1<<n) - 1
        
        dp = [[-1 for i in range(n)] for j in range(1<<n)]
       
        def solve(mask, parent, src):
            if mask == visited_all:
                return cost[parent][src]
            
            if dp[mask][parent] != -1:
                return dp[mask][parent] 
            
            res = float('inf')
            for city in range(n):
                if (1<< city) & mask == 0:
                    
                    ans = cost[parent][city] + solve( mask|(1<<city), city, src)
                    
                    res = min(res, ans)
            
            dp[mask][parent] = res
            
            return dp[mask][parent]
            
        return solve(1, 0, 0)
            