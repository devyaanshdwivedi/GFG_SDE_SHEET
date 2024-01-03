class Solution:
    def wordBoggle(self, board, dictionary):
        result = []
        trie = {}

        def insert(word):
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = True

        for word in dictionary:
            insert(word)

        def dfs(i, j, node, current_word):
            if '$' in node:
                result.append(current_word)
                del node['$']

            char = board[i][j]
            board[i][j] = '#'  # Mark the cell as visited

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and board[new_i][new_j] != '#' and board[new_i][new_j] in node:
                    dfs(new_i, new_j, node[board[new_i][new_j]], current_word + board[new_i][new_j])

            board[i][j] = char  # Restore the cell

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j])

        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends