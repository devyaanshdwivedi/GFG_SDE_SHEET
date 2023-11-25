#User function Template for python3

class Solution:
    def toyCount(self, N, k, arr):
        # code here
        arr.sort()
        i=0
        while k>=0 and i<N:
            k-=arr[i]
            i+=1
        return i if i==N else i-1

