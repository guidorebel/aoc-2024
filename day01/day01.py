
left = []
right = []

f = open("day01\\input.txt")
for line in f.readlines():
    values = [int(i) for i in line.split()]
    left.append(values[0])
    right.append(values[1])

left.sort()
right.sort()

# Part 1

total = 0
for i, value in enumerate(left):
    total += abs(left[i] - right[i])
print (total)


# Part 2

total = 0
for i, value in enumerate(left):
    total += value * right.count(value)
print (total)
