#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        left = n-1
        right = 0
        while left >=0 and right< m and arr2[right] < arr1[left]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            right+=1
            left-=1
        
        arr1.sort()
        arr2.sort()



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code EndsMerge Without Extra Space
