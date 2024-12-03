

def isAccending(data):
    for i in range(len(data)-1):
        if data[i+1] <= data[i]:
            return False
    return True


def isDecending(data):
    for i in range(len(data)-1):
        if data[i+1] >= data[i]:
            return False
    return True


def maxGap(data):
    maxGap = 0
    for i in range(len(data)-1):
        maxGap = max(maxGap, abs(data[i+1]-data[i]))
    return maxGap


def isSafe(data):
    if isAccending(data) or isDecending(data):
        if maxGap(data) <= 3:
            return True        
    return False


def makeAssending(data):
    for i in range(len(data)-1):
        newdata = data[:i] + data[i+1:]
        if isAccending(newdata): return newdata
    return data


def makeDecending(data):
    for i in range(len(data)-1):
        newdata = data[:i] + data[i+1:]
        if isDecending(newdata): return newdata
    return data


def isSafeDampened(data:list):

    if isSafe(data): return True

    for i in range(len(data)):
        newdata = data.copy()
        newdata.pop(i)
        if isSafe(newdata): return True
    
    return False


data = []
f = open("day02\\input.txt")
for line in f.readlines():
    data.append ([int(i) for i in line.split()])


nSafe = 0
for report in data:
    if isSafe(report): nSafe += 1
print (nSafe)


nSafe = 0
for report in data:
    if isSafeDampened(report): nSafe += 1
print (nSafe)