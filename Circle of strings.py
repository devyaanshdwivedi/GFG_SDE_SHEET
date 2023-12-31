#User function Template for python3


def getIndex(char):
    return ord(char) - ord('a')

class Node:
    def __init__(self):
        self.visited = False
        self.incoming = []
        self.outgoing = []
    
class Solution:
    def visit(self, node):
        node.visited = True
        for o in node.outgoing:
            if not o.visited:
                self.visit(o)
    
    def isCircle(self, N, A):
        nodes = [Node() for i in range(26)]
        for s in A:
            nodes[getIndex(s[0])].outgoing.append(nodes[getIndex(s[-1])])
            nodes[getIndex(s[-1])].incoming.append(nodes[getIndex(s[0])])
        for node in nodes:
            if len(node.incoming) != len(node.outgoing):
                return 0

        # Check that there is a single connected component.
        self.visit(nodes[getIndex(A[0][0])])
        for node in nodes:
            if len(node.incoming) != 0 and not node.visited:
                return 0
        return 1
