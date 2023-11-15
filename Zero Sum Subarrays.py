#User function Template for python3

class Solution:
    # Function to count subarrays with sum equal to 0.
    def findSubArrays(self, arr, n):
        prefix_sum = {0: 1}
        current_sum = 0
        count = 0

        for num in arr:
            current_sum += num
            if current_sum in prefix_sum:
                count += prefix_sum[current_sum]
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends