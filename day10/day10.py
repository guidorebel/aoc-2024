

dirs = [(1,0), (-1,0), (0,1), (0,-1)]


class DataGrid():

    def __init__(self, fname):

        f = open(fname)
        data = f.read()
        f.close()

        self.data = data.split("\n")
        self.rows = len(self.data)
        self.cols = len(self.data[0])

        self.value_invalid = -1
        self.value_outofbounds = -1

    def get (self, x, y):

        if 0 <= x < self.cols and 0 <= y < self.rows:
            try: return int(self.data[y][x])
            except: return self.value_invalid
        else: return self.value_outofbounds


def findTrails (grid, startnode):

    nodes = []
    endnodes = []
    trails = 0

    # Add the start node to the list
    nodes.append(startnode)

    # Traverse the tree by visiting the nodes
    while len(nodes) > 0:

        x, y = nodes.pop()                              # Depth first search
        height = grid.get(x, y)

        if height == 9:                                 # This is an end point
            if (x,y) not in endnodes:
                endnodes.append( (x,y) )                # Save unique end points
            trails += 1                                 # Count nr of unique paths

        for dx, dy in dirs:                             # Search in all directions
            if grid.get(x+dx, y+dy) == height + 1:      # Is this next position one step up?
                nodes.append((x+dx, y+dy))              # Add the node to the list of nodes to be visited

    return len(endnodes), trails


grid = DataGrid ("day10\\input.txt")

score = 0
rating = 0

for y in range(grid.cols):
    for x in range(grid.rows):
        if grid.get(x, y) == 0:
            s, r = findTrails (grid, (x,y))
            score += s
            rating += r

print (f"Part 1: {score}")
print (f"Part 2: {rating}")
