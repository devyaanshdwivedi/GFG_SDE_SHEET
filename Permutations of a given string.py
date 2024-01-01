#User function Template for python3

class Solution:
    def find_permutation(self, S):
        
        def helper(xs):
            if len(xs) == 1:
                yield xs
                return
            for i, x in enumerate(xs):
                if i > 0 and xs[i] == xs[i-1]: continue
                for y in helper(xs[:i] + xs[i+1:]):
                    yield x + y
    
        s = ''.join(sorted(list(S)))
        return list(helper(s))

