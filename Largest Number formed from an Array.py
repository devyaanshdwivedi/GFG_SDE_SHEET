#User function Template for python3

#User function Template for python3
class Solution:

    def printLargest(self,arr):
        # code here
        import functools
        def comparision(a,b):
            if a+b < b+a:
                return 1
            else:
                return -1 
            
        arr.sort(key = functools.cmp_to_key(comparision))
        return "".join(map(str,arr))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends