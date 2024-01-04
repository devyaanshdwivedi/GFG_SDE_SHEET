#User function Template for python3
import  math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        if n==0:return 0
        elif n==1:return 1
        p_p = int(math.log2(n));
        ans = p_p*(1<<(p_p-1))+n-(1<<p_p)+1+ob.countSetBits(n-(1<<p_p))
        return ans
