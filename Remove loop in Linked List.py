'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        s=set()
        while head:
            if head in s or head.next in s:
                head.next=None
            s.add(head)
            
            head=head.next
        return head

