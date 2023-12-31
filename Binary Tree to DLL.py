#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):
        self.head = None
        self.prev = None
        
    def bToDLL(self,root):
        # do Code here
        
        if root!= None:
            self.bToDLL(root.left)
            
            if self.prev == None: 
                self.head = root
            else:
                root.left=self.prev
                self.prev.right=root
            self.prev = root
            self.bToDLL(root.right)
            
        if root == None:
            return root
        return self.head 

