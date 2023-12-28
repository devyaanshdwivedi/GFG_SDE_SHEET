#User function Template for python3
import sys
class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        n = len(A)
        d = dict()
        
        ans = ""
        
        for i in range(n):
            c = A[i]
            
            if c not in d:
                d[c] = (1, i)
            else:
                count = d[c][0] + 1
                d[c] = ((count, i))
               
            pos = sys.maxsize
            temp = "#"
            
            for it in d:
                if d[it][0] == 1 and d[it][1] < pos:
                    temp = it
                    pos = d[it][1]
           
            ans += temp
        
        return ans

