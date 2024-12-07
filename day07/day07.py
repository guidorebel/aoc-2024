
from itertools import product


def evaluate (operators, result, values):

    # Generate a list of possible permutations with the specified operators
    for permutation in product(operators, repeat=len(values)-1):

        # Start with the first value
        calc = values[0]

        # Go through the list of operators and apply to next value
        for operator, nextvalue in zip(permutation, values[1:]):
            if   operator == "*": calc *= nextvalue
            elif operator == "+": calc += nextvalue
            elif operator == "|": calc = int(f"{calc}{nextvalue}")

        # If the calculated value equals the result, we can stop
        if calc == result:
            return True
    
    return False


total1 = 0
total2 = 0

f = open("day07\\input.txt")
for line in f.read().split("\n"):
    
    result, values = line.split(":")
    result = int(result)
    values = list(map(int,values.strip().split(" ")))

    # Part 1: operators * +
    if evaluate ("*+", result, values): total1 += result

    # Part 2: operators * + |
    if evaluate ("*+|", result, values): total2 += result

f.close()

print (f"Part 1: {total1}")
print (f"Part 2: {total2}")