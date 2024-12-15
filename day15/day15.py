
directions = {"^": (0,-1), ">": (1,0), "<": (-1,0), "v": (0,1) }

class WarehouseItem():

    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Item {self.type} at {self.x},{self.y}"

    def canMove(self, dir, walls, boxes):

        nextx = self.x + directions[dir][0]
        nexty = self.y + directions[dir][1]

        for item in walls:
            if nextx == item.x and nexty == item.y:
                return False

        for item in boxes:
            if nextx == item.x and nexty == item.y:
                return item.canMove(dir, walls, boxes)

        return True


    def move(self, dir, boxes):

        nextx = self.x + directions[dir][0]
        nexty = self.y + directions[dir][1]

        for item in boxes:
            if nextx == item.x and nexty == item.y:
                item.move(dir, boxes)

        self.x = nextx
        self.y = nexty

    def gps(self):
        return self.x + 100 * self.y


def plotMap(width, height, walls, boxes, robot, move=None):

    if move is not None: print (move)
    
    map = []
    for q in range(height): map.append(width*["."])

    for w in walls: map[w.y][w.x] = "#"
    for b in boxes: map[b.y][b.x] = "O"
    map[robot.y][robot.x] = "@"

    for q in range(height): print ("".join(map[q]))
    print()


f = open("day15\\input.txt")
data = f.read()
f.close()

map, allmoves = data.split("\n\n")

map = map.split("\n")
allmoves = allmoves.split("\n")

walls = []
boxes = []
robot = (0,0)

for y, line in enumerate(map):
    for x, item in enumerate(line):
        if item == "#": walls.append(WarehouseItem(item, x, y))
        elif item == "O": boxes.append(WarehouseItem(item, x, y))
        elif item == "@": robot = WarehouseItem(item, x, y)

width = x+1
height = y+1

plotMap(width, height, walls, boxes, robot)

for moves in allmoves:
    for dir in moves:
        if robot.canMove(dir, walls, boxes):
            robot.move(dir, boxes)
            #plotMap(width, height, walls, boxes, robot, dir)

total = 0
for box in boxes:
    total += box.gps()
print (f"Part 1: {total}")

