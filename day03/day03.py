
from re import findall

f = open("day03\\input.txt")
data = f.read()

total1 = 0
total2 = 0
enabled = True

# Go through the data.
# Find all occurrences of mul(x,x), or the string do(), or the string don't()

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):

    # If do() was found (value in do has a value) set the state enabled to true.
	# If don't() was found (value in do is empty) set the state enabled to false.
	if do or dont:
		enabled = bool(do)

    # If the numbers were found, calculute the mul value and add it up if state is enabled.
	else:
		x = int(a) * int(b)
		total1 += x
		total2 += x * enabled

print('Part 1:', total1)
print('Part 2:', total2)