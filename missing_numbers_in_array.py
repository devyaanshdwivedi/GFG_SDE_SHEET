#User function Template for python3

class Solution:
    def missingNumber(self, array, n):
        total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
        current_sum = sum(array)  # Sum of the given array
        return total_sum - current_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends