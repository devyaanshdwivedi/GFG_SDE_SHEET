#User function Template for python3

class Solution:
    def relativeSort(self, A1, N, A2, M):
        cou = {}
        for num in A1:
            if num in cou:
                cou[num] += 1
            else:
                cou[num] = 1
        result = []
        for num in A2:
            if num in cou:
                result.extend([num] * cou[num])
                del cou[num]
        remaining = sorted(cou.keys())
        for num in remaining:
            result.extend([num] * cou[num])

        return result
    









#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends