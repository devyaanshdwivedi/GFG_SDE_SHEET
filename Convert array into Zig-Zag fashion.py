class Solution:
    def zigZag(self, arr, n):
        flag = True  # True for <, False for >
        
        for i in range(n-1):
            if (flag and arr[i] > arr[i+1]) or (not flag and arr[i] < arr[i+1]):
                # Swap elements if the condition is not met
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
            flag = not flag 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys


def isZigzag(arr, n):
    f = 1

    for i in range(1, n):
        if f:
            if arr[i-1] > arr[i]:
                return 0
        else:
            if arr[i-1] < arr[i]:
                return 0
        f = f ^ 1

    return 1

t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.zigZag(arr, n)
    check = isZigzag(arr, n)

    if check:
        print("1")
    else:
        print("0")

    t -= 1

sys.exit(0)

# } Driver Code Ends