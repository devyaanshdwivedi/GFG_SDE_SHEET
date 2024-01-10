#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        
        lis = [0]*n
        
        result  = -float('inf')
        
        for i in range(n):
            
            maxSum = 0
            
            for j in range(i,-1,-1):
                
                if(Arr[i] > Arr[j]):
                    
                    maxSum =max (maxSum, lis[j])
                    
            lis[i] = maxSum + Arr[i]
            
            result = max(result, lis[i])
        return result
