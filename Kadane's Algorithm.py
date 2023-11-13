#User function Template for python3
class Solution:
    def maxSubArraySum(self, arr, N):
        max_sum = float('-inf')  # Initialize max_sum to negative infinity
        current_sum = 0  # Initialize current_sum to 0
        
        for num in arr:
            current_sum = max(num, current_sum + num)  # Update current_sum
            max_sum = max(max_sum, current_sum)  # Update max_sum
        
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends