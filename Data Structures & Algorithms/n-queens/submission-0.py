class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create NxN grid of "."
        row = ["."] * n
        self.n = n
        #grid = [row] 
        # contains n references to ROW!!!!
        grid = [row for _ in range(n)]
        grid = [["."] * n for i in range(n)]
        self.solutions = []
        self.getSolutions(0, grid)
        return self.solutions



    def getSolutions(self, row, grid):
        if row == self.n:
            copy = ["".join(r) for r in grid]
            self.solutions.append(copy)
            return
        for col in range(self.n):
            if self.noViolations(grid, row, col):
                grid[row][col] = "Q"
                self.getSolutions(row+1, grid)
                grid[row][col] = "."
 

    def noViolations(self, grid, row, col):
        # col check
        roww = row-1
        while roww >= 0:
            if grid[roww][col] == "Q":
                return False
            roww -= 1
        
        # trailing diagonal check:
        roww, coll = row-1, col-1
        while roww >= 0 and coll >= 0:
            if grid[roww][coll] == "Q":
                return False
            roww -= 1
            coll -= 1

        # leading diagonal check:
        roww, coll = row-1, col+1
        while roww >= 0 and coll < self.n:
            if grid[roww][coll] == "Q":
                return False
            roww -= 1
            coll += 1
        return True

        

                    