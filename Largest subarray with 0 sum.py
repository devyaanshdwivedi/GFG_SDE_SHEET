#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        # Create a dictionary to store the cumulative sum and its corresponding index
        sum_dict = {0: -1}
        max_length = 0
        current_sum = 0

        for i in range(n):
            current_sum += arr[i]

            if current_sum in sum_dict:
                max_length = max(max_length, i - sum_dict[current_sum])
            else:
                sum_dict[current_sum] = i

        return max_length


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends