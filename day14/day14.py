
from re import findall
from collections import Counter

f = open ("day14\\input.txt")
data = f.read().split("\n")
f.close()

roomwidth = 101
roomheight = 103

#============================

class Robot ():
    
    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"Robot > x:{self.x} y:{self.y} vx: {self.vx} vy: {self.vy}"

    def move(self, t):        
        self.x = ( self.x + (self.vx * t) ) % roomwidth
        self.y = ( self.y + (self.vy * t) ) % roomheight

#============================

def getRobots():

    robots = []
    for line in data:
        x, y, vx, vy = [int(i) for i in findall(r'-?\d+', line)]
        r = Robot(x, y, vx, vy)
        robots.append(r)
    return robots


def getQuadrants(robots):

    quadrants = []

    for r in robots:
        if   r.x < int(roomwidth / 2) and r.y < int(roomheight / 2): quadrants.append(1)
        elif r.x > int(roomwidth / 2) and r.y < int(roomheight / 2): quadrants.append(2)
        elif r.x < int(roomwidth / 2) and r.y > int(roomheight / 2): quadrants.append(3) 
        elif r.x > int(roomwidth / 2) and r.y > int(roomheight / 2): quadrants.append(4) 

    return Counter(quadrants)


def getSafetyFactor(counter):

    safetyfactor = 1
    for v in counter.values(): safetyfactor *= v
    return safetyfactor


def plotRobots(robots):

    map = []
    for q in range(roomheight): map.append(roomwidth*["."])
    for r in robots: map[r.y][r.x] = "#"
    for q in range(roomheight): print ("".join(map[q]))
    print()


# Part 1
#============================ 

robots = getRobots()
for r in robots: r.move(100)
quadrants = getQuadrants(robots)
print (f"Part 1: {getSafetyFactor(quadrants)}")


# Part 2
#============================ 

# Assuming that the christmas tree will be visible when the safety factor value is lowest

robots = getRobots()
safetyFactors = []

for i in range(10000):
    quadrants = getQuadrants(robots)
    safetyFactors.append(getSafetyFactor(quadrants))
    for r in robots: r.move(1)

easterEggTimePoint = safetyFactors.index(min(safetyFactors))
print (f"Part 2: {easterEggTimePoint}")

# Now print the map
robots = getRobots()
for r in robots: r.move(easterEggTimePoint)
plotRobots(robots)


#============================ 

# When printing the maps on the screen, I noticed that the robots align
# differently from timepoint 8 with a sequence of 101 timepoints (the width of the room)

robots = getRobots()
for r in robots: r.move(8)

safetyFactors = []
for i in range(100):
    quadrants = getQuadrants(robots)
    safetyFactors.append(getSafetyFactor(quadrants))
    for r in robots: r.move(101)
easterEggTimePoint = 8 + 101 * safetyFactors.index(min(safetyFactors))
print (f"Part 2 (alternative 1): {easterEggTimePoint}")


#============================ 

# And I found this funny solution online. Does it do the trick? 

robots = getRobots()
easterEggTimePoint = 0
solved = False

while not solved:

    for r in robots: r.move(1)
    easterEggTimePoint += 1

    map = []
    for q in range(roomheight): map.append(roomwidth*["."])
    for r in robots: map[r.y][r.x] = "#"
    for q in range(roomheight):
        if "".join(map[q]).find("###########") >= 0:
            solved = True
            break

print (f"Part 2 (alternative 2): {easterEggTimePoint}")
