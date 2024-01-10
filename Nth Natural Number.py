#User function Template for python3

class Solution:
    def findNth(self, N):
        ans = ""
        while N > 0:
            ans = str(N % 9) + ans
            N = N // 9
        a = int(ans)
        return a
