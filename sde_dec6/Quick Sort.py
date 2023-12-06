#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low<high:
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
        
        # code here
    
    def partition(self,arr,low,high):
        pivot=arr[low]
        start=low
        end=high
        while start<=end:
            while start<=high and arr[start]<=pivot:
                start=start+1
            while arr[end]>pivot:
                end=end-1
            if start< end:
                arr[start],arr[end]=arr[end],arr[start]
        arr[low],arr[end]=arr[end],arr[low]
        return end
        
        # code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends