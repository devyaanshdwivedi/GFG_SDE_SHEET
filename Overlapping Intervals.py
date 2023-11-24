class Solution:
    def overlappedInterval(self, Intervals):
        #Code here
        Intervals.sort(key=lambda x:x[0])
        selected = []
        selected.append(Intervals[0])
        i = 1
        while i < len(Intervals):
            if Intervals[i][0] > selected[-1][1]:
                selected.append(Intervals[i])
            else:
                selected[-1][1] = max(Intervals[i][1], selected[-1][1])
            i += 1
        return selected

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends