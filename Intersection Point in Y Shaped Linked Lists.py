#User function Template for python3
'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.
    
    Function Arguments: head_a, head_b (heads of both the lists)
    
    Return Type: value in NODE present at the point of intersection
                 or -1 if no common point.

    Contributed By: Nagendra Jha

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1, head2):
    def length(head):
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        return size

    l1 = length(head1)
    l2 = length(head2)

    start1 = head1
    start2 = head2

    if l1 > l2:
        for i in range(l1 - l2):
            start1 = start1.next
    else:
        for i in range(l2 - l1):
            start2 = start2.next

    while start1 and start2:
        if start1 == start2:
            return start1.data
        start1 = start1.next
        start2 = start2.next

    return -1  # No intersection found