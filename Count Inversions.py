# User function Template for python3
class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        if n <= 1:
            return 0

        # Split the array into two halves
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive calls to count inversions in each half
        inv_count = self.inversionCount(left, mid) + self.inversionCount(right, n - mid)

        # Merge the two halves and count inversions during the merge
        i, j, k = 0, 0, 0
        while i < mid and j < n - mid:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                # Count inversions
                inv_count += (mid - i)
            k += 1

        # Copy the remaining elements
        while i < mid:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n - mid:
            arr[k] = right[j]
            j += 1
            k += 1

        return inv_count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends