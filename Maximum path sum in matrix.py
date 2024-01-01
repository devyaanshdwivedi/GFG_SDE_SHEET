#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        dp = [[-1 for i in range(N)]for i in range(N)]
        ans = float("-inf")
        for i in range(N):
            ans = max(ans, self.find(N, Matrix, N-1, i, dp))
        return ans
    def find(self, N, Matrix, i, j, dp):
        if j < 0 or j >= N:
            return float("-inf")
        if i == 0:
            return Matrix[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        up = self.find(N, Matrix, i-1, j, dp)
        left = self.find(N, Matrix, i-1, j-1, dp)
        right = self.find(N, Matrix, i-1, j+1, dp)
        dp[i][j] = max(up, left, right)+Matrix[i][j]
        return dp[i][j]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends