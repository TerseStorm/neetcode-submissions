class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.found = False


        def getAdj(i, j):
            adj = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
            final  = []
            for y, x in adj:
                if 0 <= y < len(board) and 0 <= x < len(board[0]):
                    final.append([y, x])
            return final

        def dfs(i, j, candidateStr, n, seen):
            if candidateStr == word:
                self.found = True
                return
            elif len(candidateStr) == len(word):
                return
            for y, x in getAdj(i, j):
                if (y,x) not in seen and board[y][x] == word[n]:
                    dfs(y, x, candidateStr + board[y][x], n+1, seen | {(y,x)})


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
 
                    dfs(row, col, word[0], 1, {(row, col)})

        return self.found