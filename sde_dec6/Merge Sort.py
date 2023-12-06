#User function Template for python3

class Solution:
    def merge(self,arr, s, m, e): 
        len1 = m - s + 1
        len2 = e - m
        arr1 = [0]*len1
        arr2 = [0]*len2
        for i in range (0,len1):
            arr1[i] = arr[i+s]
        for j in range (0, len2):
            arr2[j] = arr[j+m+1]
        i = 0
        j = 0
        k = s
        while i < len1 and j < len2:
            if(arr1[i] < arr2[j]):
                arr[k] = arr1[i]
                i+=1
            else:
                arr[k] = arr2[j]
                j+=1
            k+=1
        while i < len1:
            arr[k] = arr1[i]
            k+=1
            i+=1
        while j < len2:
            arr[k] = arr2[j]
            k+=1
            j+=1
            
    def mergeSort(self,arr, l, r):
        if l < r:
            m = (l+r)//2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)





#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends