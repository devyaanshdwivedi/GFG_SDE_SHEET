#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
#         '''
# class Solution:        
#     def maxPathSum(self, root):
#         # code here
#         def maxPath(root):
#             if not root:
#                 return 0
#         if root.left == None and root.right==None:
#             return root.data
#         left = maxPath(root.left)
#         right = maxPath(root.right)
        
#         if root.left == None:
#             return root.data + right 
#         if root.right == None:
#             return root.data + left 
        
#         self.maxSum = max(seld.maxSum,left+right+root.data)
        
#         return max(left+root.data,right+root.data)
#     if not root:
#          return 0 
#     if root.left == None and root.right == None:
#         return root.data
    
#     self.maxSum = -float('inf')
#     x = maxPath(root)
#     if root.left == None or root.right == None:
#         return max(self.maxSum,x)
#     return self.maxSum

'''
class Node:
   def init(self,val):
       self.data = val
       self.left = None
       self.right = None
'''
class Solution:        
   def maxPathSum(self, root): 
       def maxPath(root): 
           if not root:
               return 0
           if root.left == None and root.right== None:
               return root.data 
           left = maxPath(root.left)
           right = maxPath(root.right)
           # edge cases for negative val
           if root.left == None:
               return root.data + right
           if root.right == None:
               return root.data + left
           # store max of
           self.maxSum = max(self.maxSum, left+right+root.data)
           #    if leftTreePathSum < 0, rightPathSUm < 0, then it returns 0,
           # which is assumption as if current node is leaf, and start calculating the path starting from it 
           return max(left+root.data, right+root.data) 
       if not root:
           return 0
       if root.left == None and root.right== None:
           return root.data
 
       # maxSum = int_min
       self.maxSum = -float('inf')
       x = maxPath(root)
       if root.left == None or root.right == None:
           return max(self.maxSum, x)
       return self.maxSum    
            
