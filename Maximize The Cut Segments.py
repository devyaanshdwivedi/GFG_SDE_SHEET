#User function Template for python3


class Solution:
    
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            a=0
            b=0
            c=0
            if x<=i:
                a=dp[i-x]
            if y<=i:
                b=dp[i-y]
            if z<=i:
                c=dp[i-z]
            if (a==0 and b==0 and c==0):
                dp[i]=0
            else:
                dp[i]=max(1+a,1+b,1+c)
        if (dp[n]==0):
            return 0
        return dp[n]-1
