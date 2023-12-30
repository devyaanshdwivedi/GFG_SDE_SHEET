#User function Template for python3

from typing import List

class Solution:
    def uniqueRow(self, row : int, col : int, M : List[List[int]]) -> List[List[int]]:
        arr=[]
        for i in M:
            arr.append(str(i))
        #print(list(set(arr)))
        final=[]
        arr=set(arr)
        for i in M:
            if(str(i) in arr):
                final.append(i)
                arr.remove(str(i))
            #print(arr)
        return final