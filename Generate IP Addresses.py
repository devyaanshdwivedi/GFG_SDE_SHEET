#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def util(self,st,n,d,s):
        global ans
        if d==0 and int(st)>=0 and int(st)<=255:
            if st[0]=='0' and n>1:
                return 
            
            ans.append(s+st)
            return 
        
        elif n==0:
            return
        
        elif d==0:
            return 
        
        for i in range(1,n):
            num=int(st[:i])
            if num>=0 and num<=255 and st[:i][0]=='0' and i>1:
                continue
            if num>=0 and num<=255:
                self.util(st[i:],len(st[i:]),d-1,s+st[:i]+'.')
        return
        
        
    def genIp(self, s):
        #Code here
        global ans
        n=len(s)
        d=3
        ans=[]
        self.util(s,n,d,'')
        return ans