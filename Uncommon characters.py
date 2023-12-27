#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here 
        C=[]
        
        for i in A:
            if i not in B:
                C.append(i)
          
        for j in B:
            if j not in A:
                C.append(j)
        C.sort()
        
        unique_chars =""
        for char in C:
            if char not in unique_chars:
               unique_chars += char
        
        if len(unique_chars)==0:
            return -1
        else:
            return unique_chars
            
        
      
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends