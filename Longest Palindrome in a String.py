#User function Template for python3

class Solution:
    def longestPalin(self, S):
        # code here
        res=S[0]
        for i in range(len(S)):
            j=i+len(res)+1
            while j<len(S)+1:
                p=S[i:j]
                if p==p[::-1]:
                    res=p
                j+=1
        return res
