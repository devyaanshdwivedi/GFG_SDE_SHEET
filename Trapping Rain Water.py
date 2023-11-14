
class Solution:
    def trappingWater(self, arr, n):
        if n <= 2:
            return 0

        left, right = 0, n - 1
        maxLeft, maxRight = 0, 0
        trappedWater = 0

        while left < right:
            if arr[left] <= arr[right]:
                maxLeft = max(maxLeft, arr[left])
                trappedWater += maxLeft - arr[left]
                left += 1
            else:
                maxRight = max(maxRight, arr[right])
                trappedWater += maxRight - arr[right]
                right -= 1

        return trappedWater


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends