#User function Template for python3
from collections import deque, defaultdict 

class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        
        q = deque()
        q.append([root, 0, 0])
        
        data = []
        while q:
            curr, x, y = q.popleft()
            data.append([x, y, curr.data])
            
            if curr.left:
                q.append([curr.left, x-1, y+1])
                
            if curr.right:
                q.append([curr.right, x+1, y+1])
        
        data.sort(key=lambda item: (item[0], item[1]))
        res = []
        for _, _, val in data:
            res.append(val)
            
        return res
            
