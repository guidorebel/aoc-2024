
f = open("day01\\input.txt")
lines = f.read().split("\n")
f.close()

left = []
right = []

for line in lines:
    values = list(map(int, line.split()))
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
