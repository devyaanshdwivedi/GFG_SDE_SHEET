#User function Template for python3

from itertools import permutations
class Solution:
    def permutation(self,s):
        def permute(arr):
            if len(arr)==1:
                return [arr]
            permutations = []
            for i in range(len(arr)):
                fixed_arr = [arr[i]]
                remaining_arr = arr[:i]+arr[i+1:]
                for per in permute(remaining_arr):
                    permutations.append(fixed_arr+per)
            return permutations
            
        ans = []
        arr = list(s)
        permu = permute(arr)
        for i in permu:
            ans.append(''.join(i))
        ans.sort()
        return ans