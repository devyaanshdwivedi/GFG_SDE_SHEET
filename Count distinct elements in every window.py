
class Solution:
    def countDistinct(self, A, N, K):
        
        distinct_counts = []
        start = 0
        end = 0
        count = 0
        distinct_elements = {}

        for i in range(N):
            # Expand the window and count distinct elements
            if A[i] not in distinct_elements:
                distinct_elements[A[i]] = 1
                count += 1
            else:
                distinct_elements[A[i]] += 1

            end += 1

            # Shrink the window if it exceeds size K
            if end - start == K:
                distinct_counts.append(count)

                # Remove the element going out of the window
                distinct_elements[A[start]] -= 1
                if distinct_elements[A[start]] == 0:
                    del distinct_elements[A[start]]
                    count -= 1

                start += 1

        return distinct_counts
                
                
        
            
        
