# User function Template for Python3

from collections import deque

class Solution:
    def minThrow(self, N, arr):
        # Create a dictionary to represent the board
        board = {}
        for i in range(0, 2 * N, 2):
            board[arr[i]] = arr[i + 1]

        # Function to find the minimum number of throws using BFS
        def bfs():
            queue = deque([(1, 0)])  # (current cell, number of throws)
            visited = set()

            while queue:
                current_cell, throws = queue.popleft()

                if current_cell == 30:
                    return throws

                for i in range(1, 7):
                    next_cell = board.get(current_cell + i, current_cell + i)
                    
                    if next_cell not in visited:
                        visited.add(next_cell)
                        queue.append((next_cell, throws + 1))

            return -1

        return bfs()



        