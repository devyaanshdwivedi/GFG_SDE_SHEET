#User function Template for python3

class Solution:
    def rotateMatrix(self, M, N, mat):
        top = 0
        bottom  = M - 1
        left = 0
        right = N - 1
        
        while left < right and top < bottom:
            
            prev = mat[top+1][left]
            
            for i in range(left,right+1):
                temp = mat[top][i]
                mat[top][i] = prev
                prev = temp
            
            top += 1
            
            for i in range(top,bottom+1):
                temp = mat[i][right]
                mat[i][right] = prev
                prev = temp
            
            right -= 1
            
            for i in range(right,left-1,-1):
                temp = mat[bottom][i]
                mat[bottom][i] = prev
                prev = temp
            
            bottom -= 1
            
            for i in range(bottom,top-1,-1):
                temp = mat[i][left]
                mat[i][left] = prev
                prev = temp
                
            left += 1
            
        return mat
                
