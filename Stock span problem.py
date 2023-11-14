class Solution:
    # Function to calculate the span of stock’s price for all n days.
    def calculateSpan(self, a, n):
        # Stack to store indices of elements
        stack = []
        # List to store span values
        span = [0] * n

        for i in range(n):
            # Pop elements from stack while the current element is greater
            while stack and a[stack[-1]] <= a[i]:
                stack.pop()

            # Calculate span for the current element
            span[i] = i + 1 if not stack else i - stack[-1]

            # Push the current element's index onto the stack
            stack.append(i)

        return span


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        for i in range(n):
            print(ans[i],end=" ")
        print()            
# } Driver Code Ends