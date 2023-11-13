class Solution:
    def longestCommonPrefix(self, arr, n):
        if not arr or n == 0:
            return "-1"
        
        min_len = min(len(s) for s in arr)
        result = []

        for i in range(min_len):
            # Check if all characters at the current position i are the same
            if all(arr[j][i] == arr[0][i] for j in range(1, n)):
                result.append(arr[0][i])
            else:
                break

        # Join the characters to form the common prefix
        return "".join(result) if result else "-1"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends