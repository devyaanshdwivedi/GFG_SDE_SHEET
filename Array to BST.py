
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 

def f(start, end, nums):
    
    if start > end:
        return None 
    
    mid = (start + end) >> 1
    root = Node(nums[mid])
    root.left = f(start, mid-1, nums)
    root.right = f(mid+1, end, nums)
    return root
    
def preorder(root, res):
    
    if root is None:
        return 
    
    res.append(root.data)
    preorder(root.left, res)
    preorder(root.right, res)

class Solution:
    def sortedArrayToBST(self, nums):
        # code here
        n = len(nums)
        root = f(0, n-1, nums)
        res = []
        preorder(root, res)
        return res