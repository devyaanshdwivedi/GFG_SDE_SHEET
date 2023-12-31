#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends

#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''

import heapq
import math

class Solution:
    
    def __init__(self):
        self.max_heap = []  # max heap for the left half
        self.min_heap = []  # min heap for the right half

    def balanceHeaps(self):
        # Balance the two heaps size, such that the difference is not more than one.
        while len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        while len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def getMedian(self):
        # Return the median of the data received till now.
        if len(self.max_heap) == len(self.min_heap):
            return -(self.max_heap[0] - self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

    def insertHeaps(self, x):
        # Insert value into heaps and balance them.
        if not self.max_heap or x < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -x)
        else:
            heapq.heappush(self.min_heap, x)
        self.balanceHeaps()
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends