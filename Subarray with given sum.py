#User function Template for python3

class Solution:
    def subArraySum(self, arr, n, s):
        left, right = 0, 0
        current_sum = arr[0]
        
        while right < n:
            if current_sum == s:
                return [left + 1, right + 1]
            elif current_sum < s:
                right += 1
                if right < n:
                    current_sum += arr[right]
            else:
                current_sum -= arr[left]
                left += 1

        return [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends