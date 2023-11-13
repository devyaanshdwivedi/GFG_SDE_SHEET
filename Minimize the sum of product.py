class Solution:
    def minValue(self, a, b, n):
        # Sort both arrays in ascending order
        a.sort()
        b.sort(reverse=True)  # Sort B in descending order
        
        # Calculate the minimum sum by multiplying the corresponding elements of sorted arrays
        result = sum(x * y for x, y in zip(a, b))
        
        return result




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends