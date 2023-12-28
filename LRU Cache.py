#User function Template for python3

# design the class in the most optimal way

class Node:
    def __init__(self, dict_ind, prev, nxt, data):
        # add dict ind
        self.dict_ind = dict_ind
        self.prev = prev
        self.next = nxt
        self.data = data
    
    # def __eq__(self, other):
    #     return self.dict_ind == other.dict_ind and self.data == other.data and self.next == other.next and self.prev == other.prev

class Queue:
    def __init__(self, maxlen):
        self.head = None
        self.tail = None
        self.maxlen = maxlen
        self.curlen = 0
    
    def append(self, dict_ind, data):
        if self.head is None:
            self.head = Node(dict_ind, None, None, data)
            self.tail = self.head
        else:
            prev = self.tail
            self.tail = Node(dict_ind, prev, None, data)
            prev.next = self.tail
        self.curlen += 1
        
        
    def pop(self):
        if self.head is not None:
            nxt = self.head.next
            del self.head
            self.head = nxt
            
            if nxt is None:
                self.tail = None
            else:
                self.head.prev = None
            self.curlen-=1
                
    
    def remove_node(self, node):
        if self.head == node:
            
            self.head = self.head.next
            self.head.prev = None
            
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
    
        else:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
        
        del node
        self.curlen-=1
            
        
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        self.key_node = dict()
        self.queue = Queue(cap)
        #code here
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        prev_value = self.get(key)
        if prev_value==-1:
            self.queue.append(key, value)
            self.key_node[key] = self.queue.tail
            if self.queue.curlen > self.queue.maxlen:
                if self.key_node[self.queue.head.dict_ind].prev is None:
                    del self.key_node[self.queue.head.dict_ind]
                self.queue.pop()
        else:
            self.queue.tail.data = value
        #code here
    
        
    #Function to return value corresponding to the key.
    def get(self, key):
        try:
            node = self.key_node[key]
        except:
            return -1
        
        value = node.data
         
        self.queue.append(key, value)
        self.key_node[key] = self.queue.tail
        self.queue.remove_node(node)
        
        return value
        #code here
        
        
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends