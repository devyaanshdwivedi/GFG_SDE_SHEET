class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        # Initialize result list to store buy-sell pairs
        result = []

        # Traverse through the stock prices
        i = 0
        while i < n - 1:
            # Find local minimum as the buy day
            while i < n - 1 and A[i + 1] <= A[i]:
                i += 1

            if i == n - 1:
                break  # No profit can be made

            # Store the buy day
            buy_day = i

            # Find local maximum as the sell day
            i += 1
            while i < n and A[i] >= A[i - 1]:
                i += 1

            # Store the sell day
            sell_day = i - 1

            # Append the buy-sell pair to the result list
            result.append([buy_day, sell_day])

        return result


#{ 
 # Driver Code Starts
#Initial template for Python

def check(ans,A,p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    if(c==p):
        return 1 
    else:
        return 0

if __name__=='__main__':
	t = int(input())
	while(t>0):
		n = int(input())
		A = [int(x) for x in input().strip().split()]
		ob = Solution()
		ans = ob.stockBuySell(A,n)
		p=0
		for i in range(n-1):
		    p += max(0,A[i+1]-A[i])
		if(len(ans) == 0):
			print("No Profit",end="")
		else:
			print(check(ans,A,p),end="")
		print()
		t-=1
# } Driver Code Ends