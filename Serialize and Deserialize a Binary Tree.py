#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    if root==None:
        A.append(-1)
    else:
        A.append(root.data)
        serialize(root.left,A)
        serialize(root.right,A)

#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    return computeDeserialize(A,[0])

def computeDeserialize(A,i):
    if A[i[0]]==-1:
        i[0]+=1
        return None
    
    node = Node(A[i[0]])
    i[0]+=1
    
    node.left = computeDeserialize(A,i)
    node.right = computeDeserialize(A,i)
    
    return node
    



