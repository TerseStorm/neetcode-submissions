class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        def rowCheck(row):
            seenNumbers = set()
            for tile in row:
                if tile != "." and tile in seenNumbers:
                    return False
                elif tile != ".":
                    seenNumbers.add(tile)
            return True
        
        def colCheck(col):
            seenNumbers = set()
            for rowNo in range(0, len(board)):
                if board[rowNo][col] and board[rowNo][col] in seenNumbers:
                    return False
                elif board[rowNo][col] != ".":
                    seenNumbers.add(board[rowNo][col])
            return True

        def squareCheck(initTileX, initTileY):
            seenNumbers = set()
            for y in range(initTileY, initTileY + 3):
                for x in range(initTileX, initTileX + 3):
                    if board[y][x] and board[y][x] in seenNumbers:
                        return False
                    elif board[y][x] != ".":
                        seenNumbers.add(board[y][x])
            return True


         

        initSquareTiles = [(0, 0), (0, 3), (0, 6), (3, 0), (6, 0), (3, 3), (6, 6)]

        return all([rowCheck(row) for row in board]) and all([colCheck(col) for col in range(len(board))]) and all([squareCheck(x, y) for x, y in initSquareTiles])

