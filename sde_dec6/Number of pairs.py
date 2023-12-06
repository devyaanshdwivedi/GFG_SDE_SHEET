#User function Template for python3


from bisect import bisect as bi
class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,a,b,M,N):
        a.sort()
        b.sort()
        ans=0
       
        for X in a:
            if X==1:
                continue
            elif X==2:
                ans=ans+bi(b,1)+N-bi(b,4)
            elif X==3:
                ans=ans+bi(b,2)+N-bi(b,3)
            else:
                ans=ans+bi(b,1)+N-bi(b,X)
                
        return(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        M,N=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        ob=Solution();
        print(ob.countPairs(a,b,M,N))
        #code here
# } Driver Code Ends