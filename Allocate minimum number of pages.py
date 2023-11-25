class Solution:
    
    def findPages(self,A, N, M):    
        if(len(A)<M):
            return(-1)
        
        def isPossible(max_pages):
            division_count = 1
            curr_pages_sum = 0
            total_splits_available = 0
            
            for pages in A:
                
                if(division_count>M):
                    break
                
                curr_pages_sum+=pages
                total_splits_available+=1
                
                if(curr_pages_sum > max_pages):
                    division_count+=1
                    curr_pages_sum=pages
                    total_splits_available-=1
                    
            if(curr_pages_sum<=max_pages):
                total_splits_available-=1
                
            if(division_count==M or (division_count<M and (M-division_count)<=total_splits_available)):
                return(True)
            
            return(False)
        
        l=max(A)
        r=sum(A)+1
        
        while(l<r):
            mid=(l+r)//2
            if(isPossible(mid)):
                r=mid
            else:
                l=mid+1
        
        return(r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends