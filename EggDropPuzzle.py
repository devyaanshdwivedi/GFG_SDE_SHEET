#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        dp = [[0 for i in range(k+1)] for j in range(n+1)]
        
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = 0
                elif i == 1:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = 0
                elif j == 1:
                    dp[i][j] = 1
                else:
                    startPrevRow = 0
                    endCurrentRow = j-1
                    overallMin = float("inf")
                    while startPrevRow < len(dp[0]) and endCurrentRow >= 0:
                        overallMin = min(overallMin, max(dp[i-1][startPrevRow], dp[i][endCurrentRow]))
                        startPrevRow += 1
                        endCurrentRow -= 1
                    dp[i][j] = overallMin + 1
                    
        return dp[-1][-1]