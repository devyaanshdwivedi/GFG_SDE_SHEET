class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        n = len(nums)
        temp = [(nums[i], i) for i in range(n)]
        temp.sort()

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or temp[i][1] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = temp[j][1]
                cycle_size += 1

            if cycle_size > 0:
                ans += (cycle_size - 1)

        return ans



#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends