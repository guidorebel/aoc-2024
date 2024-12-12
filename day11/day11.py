
f = open("day11\\input.txt")
data = f.read()
f.close()


stones = list(map(int, [i for i in data.split()]))


def blink(stones):

    # The list with the new stones.
    # The order of the stones is not relevant, so we simply append the stones.
    newstones = []

    for s in stones:

        if s == 0:
            newstones.append(1)
        
        elif len(str(s)) % 2 == 0:
            a = str(s)
            mid = int(len(str(s))/2)
            newstones.append ( int(a[:mid]) )
            newstones.append ( int(a[mid:]) )
            
        else:
            newstones.append (s * 2024)

    return newstones


for n in range(25):
    stones = blink(stones)


print (len(stones))
