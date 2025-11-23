
import itertools

def getData():

    f = open("day24\\input.txt")
    data = f.read()
    f.close()

    gates = {}
    rules = []

    top, bottom = data.split("\n\n")
    for line in top.split("\n"):
        # x00: 1
        gate, signal = line.split(":")
        gates[gate] = int(signal.strip())

    for line in bottom.split("\n"):
        # x00 AND y00 -> z00
        inputs, output = line.split(" -> ")
        input1, operator, input2 = inputs.split(" ")
        rules.append((input1, input2, operator, output))

    return gates, rules


def processSignals(gates, rules):

    while len(rules) > 0:

        input1, input2, operator, output = rules.pop(0)

        if input1 in gates and input2 in gates:
            if   operator == "AND": gates[output] = gates[input1] and gates[input2] 
            elif operator == "OR" : gates[output] = gates[input1] or gates[input2]
            elif operator == "XOR": gates[output] = gates[input1] ^ gates[input2]

        else:
            rules.append((input1, input2, operator, output))

    return gates


def getValue(gates, name):

    result = 0
    for gate, value in gates.items():
        if gate.startswith(name):
            shift = int(gate.replace(name, ""))
            result += value << shift

    return result


def swapRules(rules, pair):
    i1, i2, i3, i4 = pair

    i1_input1, i1_input2, i1_operator, i1_output = rules[i1]
    i2_input1, i2_input2, i2_operator, i2_output = rules[i2]
    i3_input1, i3_input2, i3_operator, i3_output = rules[i3]
    i4_input1, i4_input2, i4_operator, i4_output = rules[i4]

    rules[11] = (i1_input1, i1_input2, i1_operator, i2_output)
    rules[12] = (i2_input1, i2_input2, i2_operator, i1_output)
    rules[13] = (i3_input1, i3_input2, i3_operator, i4_output)
    rules[14] = (i4_input1, i4_input2, i4_operator, i3_output)

    outputs = [i1_output, i2_output, i3_output, i4_output]
    return rules, outputs.sort()


gates, rules = getData()
gates = processSignals(gates, rules)
result = getValue(gates, "z")
print (f"Part 1: {result}")

gates, rules = getData()
xvalue = getValue(gates, "x")
yvalue = getValue(gates, "y")

pairs = list(itertools.combinations(range(len(rules)), 4))
for pair in pairs:
    gates, rules = getData()
    rules, outputs = swapRules(rules, pair)
    
    gates = processSignals(gates, rules)
    if getValue(gates, "z") == xvalue + yvalue:
        print (",".join(outputs))
