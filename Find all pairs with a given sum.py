class Solution:
    def allPairs(self, A, B, N, M, X):
        # Sort arrays A and B
        A.sort()
        B.sort()
        
        pairs = []
        i = 0
        j = M - 1
        
        while i < N and j >= 0:
            curr_sum = A[i] + B[j]
            
            if curr_sum == X:
                pairs.append((A[i], B[j]))
                i += 1
                j -= 1
            elif curr_sum < X:
                i += 1
            else:
                j -= 1
        
        return pairs
