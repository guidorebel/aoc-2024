

def getdisk():

    f = open("day09\\input.txt")
    data = [v for v in f.read()]
    f.close()

    disk = []

    # Go through the disk map.
    # Each odd value is a file length.
    # Each even value is a free space length.
    for index, blocklength in enumerate(data):

        if index % 2 == 0:  disk += int(blocklength) * [str(int(index/2))]
        else:               disk += int(blocklength) * ["."]
        
    return disk


def getchecksum(disk):

    total = 0
    for index, fileid in enumerate(disk):
        try: total += index * int(fileid)
        except: pass
    return total


def part1():

    disk = getdisk()

    index_l = 0
    index_r = len(disk)-1

    # Go through the disk from the left
    for index_l in range(len(disk)):

        # If the left index exceeds the right index, we are done. 
        if index_l >= index_r: break

        # Find the first free spot
        if disk[index_l] == ".":
        
            # Find the first file reference
            while disk[index_r] == ".": 
                index_r -= 1
            
            # Move part of the file to new location
            disk[index_l] = disk[index_r]

            # Erase the original location
            disk[index_r] = "."


    print (f"Part 1: {getchecksum(disk)}")



def part2():

    disk = getdisk()

    # Build a lost of free positions and lengths
    free = []
    start = 0
    pos = disk.index(".", start)
    while pos>0:
        l = 1
        while (disk[pos+l] == "."): l+=1
        free.append( (pos, l))
        start = pos + l

        try: pos = disk.index(".", start)
        except: pos = -1


    # Reverse through the disk and try to move files
    start = len(disk) - 1

    while start >= 0:

        # Find the first reference to next file ID, and get the length
        while disk[start] == ".": start -= 1
        
        fileID = disk[start]
        l = 1
        while (disk[start-l] == fileID): l += 1

        # Search through the list with free disk space to see if we can move the file
        for ifree, (pfree, lfree) in enumerate(free):

            # If there is no free disk space to the left, break            
            if pfree >= start: break
            
            # If there is free disk space, move the file ID
            if lfree >= l:
                
                disk[pfree:pfree + l] = l * [str(fileID)]
                free[ifree] = (pfree+l, lfree-l)
                disk[start-l+1 : start+1] = l * ["."]

                break

        start -= l

    print (f"Part 2: {getchecksum(disk)}")


part1 ()
part2 ()