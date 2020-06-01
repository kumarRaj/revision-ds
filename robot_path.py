grid = (3,2)

class Robot:
    def findPath(self, currentPosition, grid):
        uniquePaths = 0
        if self.canMoveRight(currentPosition, grid):
            newPosition = self.moveRight(currentPosition)
            if self.isGridEnd(newPosition, grid):
                uniquePaths += 1
            else: 
                uniquePaths += self.findPath(newPosition, grid)

        if self.canMoveDown(currentPosition, grid):
            newPosition = self.moveDown(currentPosition)
            if self.isGridEnd(newPosition, grid):
                uniquePaths += 1
            else: 
                uniquePaths += self.findPath(newPosition, grid)

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


print(Robot().findPath((0,0), grid))