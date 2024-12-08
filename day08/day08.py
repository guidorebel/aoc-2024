
from collections import defaultdict

class DataGrid():

    def __init__(self, data):
        self.grid = []
        for line in data.split("\n"): self.grid.append([i for i in line])
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def get (self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.grid[y][x]
        return None

    def set (self, x, y, v):
        self.grid[y][x] = v



f = open("day08\\input.txt")
data = f.read()
f.close()

grid = DataGrid(data)

antenas = defaultdict(list)

antinodes_part1 = []
antinodes_part2 = []

for y in range(grid.rows):
    for x in range(grid.cols):
        if grid.get(x, y) != ".":
            antenas[grid.get(x,y)].append((x,y))


for key, values in antenas.items():

    for i in range(len(values)):
        for j in range(len(values)):
            if i == j:
                continue
            else:

                delta_x = values[i][0] - values[j][0]
                delta_y = values[i][1] - values[j][1]

                multiplier = 0

                while True:
                    antinode_x = values[i][0] + (multiplier * delta_x)
                    antinode_y = values[i][1] + (multiplier * delta_y)

                    if 0 <= antinode_x < grid.cols:
                        if 0 <= antinode_y < grid.rows:

                            if not (antinode_x, antinode_y) in antinodes_part2: antinodes_part2.append( (antinode_x, antinode_y) )

                            if multiplier == 1:
                                if not (antinode_x, antinode_y) in antinodes_part1: antinodes_part1.append( (antinode_x, antinode_y) )

                        else: break
                    else: break

                    multiplier += 1
                    

print (f"Part 1: {len(antinodes_part1)}")
print (f"Part 2: {len(antinodes_part2)}")
