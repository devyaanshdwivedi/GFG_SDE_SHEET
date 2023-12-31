#User function Template for python3

class Solution:
    def palindromepair(self, N, arr):
      # code here 
        ans = set()
        index = {word:i for i, word in enumerate(arr)}
        for i, word in enumerate(arr):
            for j in range(len(word)+1):
                left = word[:j]
                right = word[j:]
                if left==left[::-1]:
                    if right[::-1] in index and index[right[::-1]]!=i:
                        ans.add((index[right[::-1]], i))
                    if len(ans)>0:
                        return 1
                if right==right[::-1]:
                    if left[::-1] in index and index[left[::-1]]!=i:
                        ans.add((i, index[left[::-1]]))
                    if len(ans)>0:
                        return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        for i in range(N):
            s = input()
            arr.append(s)
        
        ob = Solution()
        print(ob.palindromepair(N,arr))
# } Driver Code Ends