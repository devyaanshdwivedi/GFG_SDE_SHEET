#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        
        m = [[0 for j in range(len(S2)+1)] for i in range(len(S1)+1)]
        
        res =  0
        for i in range(len(S1)-1,-1,-1):
            for j in range(len(S2)-1,-1,-1):
                if S1[i] == S2[j]:
                    m[i][j] = 1 + m[i+1][j+1]
                    res = max(res,m[i][j])

                    
        return res