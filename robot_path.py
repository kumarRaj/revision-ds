grid = (3,2)

class Robot:
    def __init__(self):
        self.dpMap = {}

    
    def findPath(self, currentPosition, grid):
        def __init__(self):
            None
        if currentPosition in self.dpMap:
            return self.dpMap[currentPosition]
        uniquePaths = 0
        if self.isGridEnd(currentPosition, grid):
            uniquePaths += 1

        if self.canMoveRight(currentPosition, grid):
            newPosition = self.moveRight(currentPosition)
            uniquePaths += self.findPath(newPosition, grid)

        if self.canMoveDown(currentPosition, grid):
            newPosition = self.moveDown(currentPosition)
            uniquePaths += self.findPath(newPosition, grid)
        self.dpMap[currentPosition] = uniquePaths
        return uniquePaths

    def isGridEnd(self, currentPosition, grid):
        if not grid:
            return True
        x = grid[0] - 1
        y = grid[1] - 1
        return currentPosition == (x,y)

    def canMoveRight(self, currentPosition, grid):
        return currentPosition[1] < grid[1] - 1
    def canMoveDown(self, currentPosition, grid):
        return currentPosition[0] < grid[0] - 1
    def moveRight(self, currentPosition):
        return (currentPosition[0], currentPosition[1] + 1)
    def moveDown(self, currentPosition):
        return (currentPosition[0] + 1, currentPosition[1])
