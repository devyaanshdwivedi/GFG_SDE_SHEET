#User function Template for python3

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat):
        for i in range(len(Str)):
            if Str[i] in pat:
                return i
        return -1

                
