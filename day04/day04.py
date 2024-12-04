
XMAS = "XMAS"
directions = [ [1,0], [1,1], [1,-1], [0,1], [0,-1], [-1,0], [-1,1], [-1,-1] ]

class DataGrid():

    def __init__(self, data):
        self.data = data.split("\n")
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def get (self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.data[y][x]
        return None
    
    def dim (self):
        return self.cols, self.rows


def findXMAS(data:DataGrid, index, x, y, d):
    
    if data.get(x, y) == XMAS[index]:
        
        if index == len(XMAS)-1:
            # We found XMAS!
            return 1
        else:
            # Keep searching in the current direction
            return findXMAS(data, index+1, x+d[0], y+d[1], d)
    
    # XMAS was not found.
    else: return 0


def findXmas(data:DataGrid, x, y):
    
    if data.get(x, y) == "A":
        if (data.get(x-1,y-1) == "M" and data.get(x+1,y+1) == "S") or data.get(x-1,y-1) == "S" and data.get(x+1,y+1) == "M":
            if (data.get(x-1,y+1) == "M" and data.get(x+1,y-1) == "S") or data.get(x-1,y+1) == "S" and data.get(x+1,y-1) == "M":
                return 1
        
    return 0


f = open ("day04\\input.txt")
data = f.read()
f.close()

grid = DataGrid(data)
xdim, ydim = grid.dim()

count = 0
# Go through the grid
for y in range(ydim):
    for x in range(xdim):
        # Search in all directions
        for dir in directions:
            # Search for all characters in XMAS
            count += findXMAS(grid, 0, x, y, dir)
print (f"Part 1: {count}")

count = 0
# Go through the grid
for y in range(ydim):
    for x in range(xdim):
        # Search for all characters in MAS in an X shape
        count += findXmas(grid, x, y)
print (f"Part 2: {count}")
