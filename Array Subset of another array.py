# User function to check if a2 is a subset of a1
def isSubset(a1, a2, n, m):
    # Create dictionaries to store the count of each element in a1 and a2
    count_a1 = {}
    count_a2 = {}

    # Count occurrences in a1
    for element in a1:
        count_a1[element] = count_a1.get(element, 0) + 1

    # Count occurrences in a2
    for element in a2:
        count_a2[element] = count_a2.get(element, 0) + 1

    # Check if all elements in a2 have counts less than or equal to their counts in a1
    for element, count in count_a2.items():
        if element not in count_a1 or count_a1[element] < count:
            return "No"

    return "Yes"
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends