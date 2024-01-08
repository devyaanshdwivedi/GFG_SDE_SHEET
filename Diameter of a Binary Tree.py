#User function Template for python3



class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        if root==None:
            return 0
        ct=[0]
        def dfs(root,ct):
            if root==None:
                return 0
            a=dfs(root.left,ct)
            b=dfs(root.right,ct)
            ct[0]=max(ct[0],a+b)
            return max(a,b)+1
        dfs(root,ct)
        return ct[0]+1
        # Code here
