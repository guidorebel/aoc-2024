
f = open("day25\\input.txt")
data = f.read()
f.close()

class Key():

    def __init__(self, lines):

        self.heights = [0,0,0,0,0]
        for index, line in enumerate(lines):
            if index > 0 and index < 6:
                for i, v in enumerate(line):
                    if v == "#": self.heights[i] += 1

    def __repr__(self):
        return f"Key with heights {",".join ( [str(i) for i in self.heights ] ) }"

class Lock():

    def __init__(self, lines):

        self.heights = [0,0,0,0,0]
        for index, line in enumerate(lines):
            if index > 0 and index < 6:
                for i, v in enumerate(line):
                    if v == "#": self.heights[i] += 1


    def canFit(self, key):

        canFit = True
        for i in range(len(self.heights)):
            if self.heights[i] + key.heights[i] > 5:
                canFit = False
        return canFit


    def __repr__(self):
        return f"Lock with heights {",".join ( [str(i) for i in self.heights ] ) }"


keys = []
locks = []

items = data.split("\n\n")

for item in items:
    lines = item.split("\n")
    if   lines[0] == "#####": locks.append(Lock(lines))
    elif lines[0] == ".....": keys.append(Key(lines))

print (keys)
print (locks)

count = 0
for lock in locks:
    for key in keys:
        if lock.canFit(key): count += 1

print (f"Part 1: {count}")