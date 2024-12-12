

dirs = [(1,0), (-1,0), (0,1), (0,-1)]


class DataGrid():

    def __init__(self, fname):

        f = open(fname)
        data = f.read()
        f.close()

        self.data = data.split("\n")
        self.rows = len(self.data)
        self.cols = len(self.data[0])

        self.value_outofbounds = "."

    def get (self, x, y):

        if 0 <= x < self.cols and 0 <= y < self.rows:
            try: return self.data[y][x]
            except: return self.value_invalid
        else: return self.value_outofbounds



def growRegion (grid, plant, start):

    tovisit = set()
    visited = set()
    
    area = 0
    perimeter = 0
    sides = 0

    # Add the start coordinate to the list
    tovisit.add(start)

    # Search the coordinates for the expected plant value
    while len(tovisit) > 0:

        x, y = tovisit.pop()

        if grid.get(x, y) == plant:

            area += 1
            visited.add ((x,y))

            # Search the neighbouring coordinates for the expected plant value
            for dx, dy in dirs:
                if grid.get(x+dx, y+dy) == plant:
                    if not (x+dx,y+dy) in visited:
                        # Add this coordinate to the list
                        tovisit.add((x+dx, y+dy))
                else:
                    perimeter += 1


    # Count the nr of sides, which is equal to the nr of corners.
    # Corners can be found by checking neighbouring values.
    # 
    # .  .  .
    # .  x  x    the x in the middle has two outer corners
    # .  .  .
    #
    # .  x  .
    # x  x  x    the x in the middle has four inner corners
    # .  x  .

    for x, y in visited:

        # Outer corners have two sides that are not in the visited region
        if (x-1, y) not in visited and (x, y-1) not in visited: sides += 1
        if (x-1, y) not in visited and (x, y+1) not in visited: sides += 1
        if (x+1, y) not in visited and (x, y-1) not in visited: sides += 1
        if (x+1, y) not in visited and (x, y+1) not in visited: sides += 1

        # Inner corners have two sides that are in the visited region, and the opposite coordinate is not in the visited region
        if (x-1, y) in visited and (x, y-1) in visited and (x-1, y-1) not in visited: sides += 1
        if (x-1, y) in visited and (x, y+1) in visited and (x-1, y+1) not in visited: sides += 1
        if (x+1, y) in visited and (x, y-1) in visited and (x+1, y-1) not in visited: sides += 1
        if (x+1, y) in visited and (x, y+1) in visited and (x+1, y+1) not in visited: sides += 1

    return visited, area, perimeter, sides



grid = DataGrid ("day12\\input.txt")

visited = set()

price1 = 0
price2 = 0

for y in range (grid.rows):
    for x in range (grid.cols):
        if not (x,y) in visited:
            v, a, p, s = growRegion(grid, grid.get (x,y), (x,y))

            p1 = a * p     # print (f"A region of {grid.get (x,y)} plants with price {a} * {p} = {p1}")
            p2 = a * s     # print (f"A region of {grid.get (x,y)} plants with price {a} * {s} = {p2}")

            visited.update (v)
            price1 += p1
            price2 += p2

print (f"Part 1: {price1}")
print (f"Part 2: {price2}")
