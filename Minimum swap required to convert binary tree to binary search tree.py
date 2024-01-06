from typing import List


class Solution:
    def minSwaps(self, n : int, A : List[int]) -> int:
        # code here
        ans = []
        
        def inorder(i):
            if i >= n:
                return
            inorder(2*i+1)
            ans.append(A[i])
            inorder(2*i+2)
        inorder(0)
        
        cnt = 0
        t = sorted((e, i) for i, e in enumerate(ans))
        visited = set()
        for i, (_, j) in enumerate(t):
            if j not in visited:
                visited.add(i)
                d = i
                while i != j:
                    #A[d] = A[j]
                    visited.add(j)
                    d = t[d][1]
                    j = t[d][1]
                    cnt += 1
        return cnt

