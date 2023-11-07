class Solution:
    def leaders(self, A, N):
        leaders_list = []
        max_right = A[N - 1]  # The rightmost element is always a leader
        leaders_list.append(max_right)

        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                leaders_list.append(A[i])
                max_right = A[i]

        return leaders_list[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends