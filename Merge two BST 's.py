#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    #Function to return a list of integers denoting the node 
    #values of both the BST in a sorted order.
    def merge(self, root1, root2):
        result = []
        stack1, stack2 = [], []
        current1, current2 = root1, root2
        
        # Perform in-order traversal of both BSTs simultaneously
        while stack1 or current1 or stack2 or current2:
            while current1:
                stack1.append(current1)
                current1 = current1.left
            while current2:
                stack2.append(current2)
                current2 = current2.left
            
            # Compare the top elements of both stacks
            if not stack2 or (stack1 and stack1[-1].data <= stack2[-1].data):
                current1 = stack1.pop()
                result.append(current1.data)
                current1 = current1.right
            else:
                current2 = stack2.pop()
                result.append(current2.data)
                current2 = current2.right
        
        return result