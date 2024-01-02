#User function Template for python3

class Solution:
    def rremove (self, s):
        new_str = ""
        i = 0
        flag = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    i += 1
                    flag = 1
            else:
                new_str += s[i]
            i += 1
        
        if flag != 0:
            return self.rremove(new_str)
        return new_str



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends