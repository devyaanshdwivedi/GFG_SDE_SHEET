class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)

        low, high = max(0, k - m), min(k, n)

        while low <= high:
            i = (low + high) // 2
            j = k - i

            if i < n and j > 0 and arr2[j - 1] > arr1[i]:
                # Increase i
                low = i + 1
            elif i > 0 and j < m and arr1[i - 1] > arr2[j]:
                # Decrease i
                high = i - 1
            else:
                # Found the correct partition
                if i == 0:
                    return arr2[j - 1]
                elif j == 0:
                    return arr1[i - 1]
                else:
                    return max(arr1[i - 1], arr2[j - 1])

