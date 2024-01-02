from functools import lru_cache
class Solution:
    def editDistance(self, s, t):
           # Code here
        @lru_cache(None)
        def solve(i,j):
            if i==len(s) or j==len(t):
                return len(s)-i + len(t)-j
                
            if s[i]==t[j]:
                return solve(i+1,j+1)
            else:
                return 1+min(solve(i+1,j),solve(i+1,j+1),solve(i,j+1))
          
        return solve(0,0)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends