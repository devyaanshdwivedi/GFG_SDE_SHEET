class Solution:
    def optimalKeys(self, N):
        dp = [ 0 for i in range(N+1) ]

        for i in range(1, N+1):
            dp[i] = dp[i-1] + 1
            j = 2
            while j < i:
                dp[i] = max(dp[i], dp[j-2] * (i - j + 1))
                j += 1

        return dp[N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.optimalKeys(N))
# } Driver Code Ends