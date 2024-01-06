from typing import List

class Solution:
    def maxHeight(self, N: int, A: List[int], M: int) -> int:
        def woodCut(height):
            total_wood = 0
            for h in A:
                if h > height:
                    total_wood += h - height
            return total_wood

        low, high = 0, max(A)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if woodCut(mid) >= M:
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
