

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


def growRegion (grid, region, start):

    tovisit = set()
    visited = set()
    
    area = 0
    perimeter = 0

    # Add the start coordinate to the list
    tovisit.add(start)

    # Search the coordinates for the same value
    while len(tovisit) > 0:

        x, y = tovisit.pop()

        r = grid.get(x, y)
        if r == region:

            area += 1
            visited.add ( (x,y) )

            for dx, dy in dirs:
                if grid.get(x+dx, y+dy) == region:
                    if not (x+dx,y+dy) in visited:
                        tovisit.add((x+dx, y+dy))
                else:
                    perimeter += 1

    price = area * perimeter
    print (f"A region of {region} plants with price {area} * {perimeter} = {price}")

    return visited, price



grid = DataGrid ("day12\\input.txt")


visited = set()
price = 0

for y in range (grid.rows):
    for x in range (grid.cols):
        if not (x,y) in visited:
            v, p = growRegion(grid, grid.get (x,y), (x,y))
            visited.update (v)
            price += p

print (price)