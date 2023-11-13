class Solution:
    def partition(self, arr, l, r):
        pivot = arr[r]
        i = l - 1
        
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1
    
    def kthSmallestUtil(self, arr, l, r, k):
        if l <= r:
            pivot_index = self.partition(arr, l, r)
            
            if pivot_index == k:
                return arr[pivot_index]
            elif pivot_index < k:
                return self.kthSmallestUtil(arr, pivot_index + 1, r, k)
            else:
                return self.kthSmallestUtil(arr, l, pivot_index - 1, k)
    
    def kthSmallest(self, arr, l, r, k):
        return self.kthSmallestUtil(arr, l, r, k - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends