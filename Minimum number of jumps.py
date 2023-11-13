class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0  # No jumps needed for an array of length 1 or less
        
        if arr[0] == 0:
            return -1  # Cannot move if the first element is 0
        
        max_reach = arr[0]  # Maximum index that can be reached
        steps = arr[0]  # Remaining steps to be taken
        jumps = 1  # Number of jumps
        
        for i in range(1, n):
            if i == n - 1:
                return jumps  # Reached the end of the array
            
            max_reach = max(max_reach, i + arr[i])  # Update the maximum index that can be reached
            
            steps -= 1  # Use one step
            
            if steps == 0:
                jumps += 1  # Need to take a jump
                
                if i >= max_reach:
                    return -1  # Cannot reach the end if current index is greater than or equal to max_reach
                
                steps = max_reach - i  # Remaining steps to be taken is the difference between max_reach and current index


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends