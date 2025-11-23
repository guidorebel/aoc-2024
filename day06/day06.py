
from collections import deque

UP    = ( 0,-1)
DOWN  = ( 0, 1)
LEFT  = (-1, 0)
RIGHT = ( 1, 0)
DIRECTIONS = deque ([UP, RIGHT, DOWN, LEFT])


class DataGrid():

    def __init__(self, fname):

        f = open("day06\\input.txt")
        data = f.read()
        f.close()

        self.grid = [ [v for v in line] for line in data.split("\n")]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self.v_invalid = "-"
        self.v_outofbounds = "@"

    def get (self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            try: return self.grid[y][x]
            except: return self.v_invalid
        else: return self.v_outofbounds

    def set (self, x, y, v):
        self.grid[y][x] = v


def getDataGrid():

    grid = DataGrid("day06\\input.txt")

    for j in range(grid.rows):
        for i in range(grid.cols):
            if grid.get(i,j) == "^":
                x, y = i, j
                grid.set(x,y,".")

    return grid, x, y


def walkOfGrid (grid, x, y):

    visited = []
    inGrid = True

    while inGrid:

        if not (x,y) in visited:
            visited.append((x,y))

        # Calculate our next position
        dx, dy = DIRECTIONS[0]
        next_x, next_y = x + dx, y + dy

        # If there is nothing in our our way, step forward
        if grid.get(next_x, next_y) == ".":
            x, y = next_x, next_y
                
        # It there is something in our way, rotate, and step forward
        else:
            
            DIRECTIONS.rotate(-1)
            dx, dy = DIRECTIONS[0]
            x, y = x + dx, y + dy
        
        # Check if we are still in the grid
        if grid.get(next_x, next_y) == "@":
            inGrid = False


    return len (visited)


grid, x, y = getDataGrid()
count = walkOfGrid(grid, x, y)
print (f"Part 1: { count }")

