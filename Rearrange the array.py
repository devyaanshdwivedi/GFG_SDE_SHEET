#User function Template for python3
class Solution:
    def rearrangeArray(self,n,arr):
        #code here
        arr = [0] + arr
        ans = 1
        def gcd(a,b):
            if a < b:
                t = a
                a = b
                b = t
            if a%b == 0:
                return b;
            else:
                return gcd(b,a%b);
        vis = [False for _ in range(n+1)]
        for i in range(1,n+1):
            if not vis[i]:
                index = i
                move = 1
                vis[index] = True
                while arr[index] != i:
                    move += 1
                    index = arr[index]
                    vis[index] = True
                tt = gcd(ans,move);
                ans = (ans//tt)*move
        return ans%int(1e9+7)



