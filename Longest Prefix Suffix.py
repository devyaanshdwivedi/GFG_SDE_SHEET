#User function Template for python3

class Solution:
    def lps(self, s):
        n = len(s)
        prefix = [0] * n
        i, j = 0, 1
        while j < n:
            if s[i] == s[j]:
                prefix[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = prefix[i - 1]

        a = s[:i]
        return len(a)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends