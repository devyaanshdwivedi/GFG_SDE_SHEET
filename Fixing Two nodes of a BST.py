#User function Template for python3


def fix_BST(root, prev, first, mid, last):
    
    if root is None:
        return 
    
    fix_BST(root.left, prev, first, mid, last)
    
    if prev[0]:
        if root.data < prev[0].data:
            if first[0] is None:
                first[0] = prev[0]
                mid[0] = root
            else:
                last[0] = root
        
    prev[0] = root
    
    fix_BST(root.right, prev, first, mid, last)

#Function to fix a given BST where two nodes are swapped.  
class Solution:
    def correctBST(self, root):
    # code here
    
        prev = [None]
        first = [None]
        mid = [None]
        last = [None]
    
        fix_BST(root, prev, first, mid, last)
    
        if last[0]:
            first[0].data, last[0].data = last[0].data, first[0].data 
        else:
            first[0].data, mid[0].data = mid[0].data, first[0].data 
        