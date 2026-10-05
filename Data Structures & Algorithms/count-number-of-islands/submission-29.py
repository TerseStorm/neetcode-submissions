# I regard this as a test of your data structures knowledge. The algorithm was sound, but the data structures used ballooned the running time to more than it needed to be.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.seenIndices = set()
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1" and (y, x) not in self.seenIndices:
                    count += 1
                    self.explore(grid, (y, x))
            
        return count


    def explore(self, grid, root):
        queue = [root]
        while queue:
            cur = queue.pop(0)
            neighbours = self.getNeighbours(grid, cur)
            queue = self.safeExtend(queue, self.seenIndices, neighbours)
            self.safeExtendList(self.seenIndices, self.seenIndices, neighbours)
    
    def safeExtend(self, list1, seen, list2):
        for item in list2:
            if item not in seen:
                list1.append(item)
        return list1

    def safeExtendList(self, list1, seen, list2):
        for item in list2:
            if item not in seen:
                list1.add(item)
        return list1

    def getNeighbours(self, grid, cur):
        neighbours = []
        if cur[0] - 1 >= 0 and grid[cur[0] - 1][cur[1]] == "1":
            neighbours.append((cur[0] - 1, cur[1]))
        if cur[0] + 1 < len(grid) and grid[cur[0] + 1][cur[1]] == "1":
            neighbours.append((cur[0] + 1, cur[1]))
        if cur[1] - 1 >= 0 and grid[cur[0]][cur[1] - 1] == "1":
            neighbours.append((cur[0], cur[1] - 1))
        if cur[1] + 1 < len(grid[0]) and grid[cur[0]][cur[1] + 1] == "1":
            neighbours.append((cur[0], cur[1] + 1))
        return neighbours

