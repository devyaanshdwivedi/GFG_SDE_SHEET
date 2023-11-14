class Solution:
    # Function to find the minimum number of platforms required.
    def minimumPlatform(self, n, arr, dep):
        # Sorting the arrival and departure arrays
        arr.sort()
        dep.sort()

        platforms_needed = 1  # Initialize the platforms_needed to 1
        result = 1  # Initialize the result to 1
        i = 1
        j = 0

        # Iterate through the arrival and departure arrays
        while i < n and j < n:

            # If the train is still at the station
            # when the next train arrives
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1

                # Update the result with the maximum
                # number of platforms needed
                result = max(result, platforms_needed)
            else:
                # If a train departs, decrease the
                # number of platforms needed
                platforms_needed -= 1
                j += 1

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends