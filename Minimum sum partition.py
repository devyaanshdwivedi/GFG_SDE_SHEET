import sys
 
class Solution:
    def minDifference(self, arr, n):
    # code here
            TotalSum = sum(arr)
            N = len(arr)
            dp = [[ False for j in range(TotalSum+1)] for i in range(N+1)]
            #print(dp)
            for i in range(N+1):
                dp[i][0] = True
                
            for j in range(1,TotalSum+1):
                dp[0][j] = False
                
            for i in range(1,N+1):
                for j in range(1,TotalSum+1):
                    
                    if arr[i-1] <= j:
                        dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
     
            possibleS1 = []
            for j in range(((TotalSum)//2)+1):
                if dp[N][j] :
                    possibleS1.append(j)
                    
            minValue = sys.maxsize
            for val in possibleS1:
                minValue = min(minValue , TotalSum - (2 * val))
     
            return minValue