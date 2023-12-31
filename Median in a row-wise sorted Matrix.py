#User function Template for python3
from bisect import bisect_right
class Solution:
    def median(self, matrix, R, C):
        #code here 
        min_no = matrix[0][0]
        max_no = 0
        for i in range(R):
            if matrix[i][0] < min_no:
                min_no = matrix[i][0]
            if matrix[i][C-1] > max_no:
                max_no = matrix[i][C-1]
        desired = (R * C + 1)//2
        while min_no < max_no:
            mid = min_no + (max_no - min_no)//2
            place = [0]
            for i in range(R):
                j = bisect_right(matrix[i],mid)
                place[0] = place[0] + j
            if place[0] < desired:
                min_no = mid + 1
            else:
                max_no = mid
        return min_no
                
                