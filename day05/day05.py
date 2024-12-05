
from collections import defaultdict

f = open("day05\\input.txt")
lines = f.read().split("\n")
f.close()

rules = []
updates = []

# Go throug all lines
for line in lines:
    # Rules
    if line.find("|")>0:    rules.append([int(i) for i in line.split("|")])
    # Updates
    elif line.find(",")>0:  updates.append([int(i) for i in line.split(",")])


def isOrdered(rules, update) -> bool:

    ordered = True

    # Go through all rules
    for rule in rules:
        x, y = rule
        # If both x and y are in update, x should be before y
        if x in update and y in update:
            xi = update.index(x)
            yi = update.index(y)
            if yi < xi:
                ordered = False
                break
    return ordered


def reOrder(rules, update):

    ordered = False

    # Keep on reordering the pages until they are ordered
    while not ordered:
        
        # Go through all rules
        for rule in rules:
            x, y = rule
            # If both x and y are in update, x should be before y
            # If they are not, simply swap them arround.
            if x in update and y in update:
                xi = update.index(x)
                yi = update.index(y)
                if yi < xi: update[xi], update[yi] = update[yi], update[xi]

        ordered = isOrdered(rules, update)

    return update

# Part 1. 
total = 0
for update in updates:
    if isOrdered(rules, update):
        total+=update[int(len(update)/2)]
print (f"Part 1: {total}")

# Part 2
total = 0
for update in updates:
    if not isOrdered(rules, update):
        update = reOrder(rules, update)
        total+=update[int(len(update)/2)]
print (f"Part 2: {total}")
