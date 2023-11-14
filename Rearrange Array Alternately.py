#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange the array elements alternately.
    def rearrange(self, arr, n):
        if n <= 1:
            return

        max_idx = n - 1
        min_idx = 0
        max_element = arr[-1] + 1

        for i in range(n):
            # If even index, pick the maximum element
            if i % 2 == 0:
                arr[i] += (arr[max_idx] % max_element) * max_element
                max_idx -= 1
            # If odd index, pick the minimum element
            else:
                arr[i] += (arr[min_idx] % max_element) * max_element
                min_idx += 1

        # Update the array with the rearranged values
        for i in range(n):
            arr[i] = arr[i] // max_element



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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends