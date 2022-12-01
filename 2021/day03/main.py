import operator

with open("input.txt", "r") as input_file:
    lines = list(map(lambda x: x.strip(), input_file.readlines()))

transpose = lambda x: ["".join(s) for s in zip(*x)]

gamma = int(
    "".join(
        [
            "1" if number.count("1") > number.count("0") else "0"
            for number in transpose(lines)
        ]
    ),
    2,
)
epsilon = ~gamma & 0xFFF  # because two's complement


bit_map = lambda li, op: {
    i: ("1" if op(col.count("1"), col.count("0")) else "0")
    for i, col in enumerate(transpose(li))
}


def calculate_gas(array, op):
    for i in range(12):
        bit = bit_map(array, op)[i]
        array = list(filter(lambda x: x[i] == bit, array))
        if len(array) == 1:
            break
    return int(array[0], 2)


o2 = calculate_gas(lines, operator.ge)
co2 = calculate_gas(lines, operator.lt)

print(f"PART 1: {gamma * epsilon}")
print(f"PART 2: {co2 * o2}")
