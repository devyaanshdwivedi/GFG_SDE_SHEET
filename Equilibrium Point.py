# User function Template for python3
class Solution:
    def equilibriumPoint(self, A, N):
        total_sum = sum(A)
        left_sum = 0

        for i in range(N):
            total_sum -= A[i]
            if left_sum == total_sum:
                return i + 1
            left_sum += A[i]

        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends