#User function Template for python3

class Solution:
    def findMidSum(self, ar1, ar2, n):
        i, j, m1, m2, count = 0, 0, -1, -1, 0
        target_count = (n * 2) // 2  # Total number of elements in the merged array

        while count <= target_count:
            if i == n:  # All elements of ar1 are merged
                m1 = m2
                m2 = ar2[j]
                j += 1
            elif j == n:  # All elements of ar2 are merged
                m1 = m2
                m2 = ar1[i]
                i += 1
            elif ar1[i] <= ar2[j]:  # Merge the smaller element from ar1
                m1 = m2
                m2 = ar1[i]
                i += 1
            else:  # Merge the smaller element from ar2
                m1 = m2
                m2 = ar2[j]
                j += 1

            count += 1

        return m1 + m2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends