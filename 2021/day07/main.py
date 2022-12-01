
with open("input.txt", "r") as input_file:
    crabs = list(map(int, input_file.read().split(",")))


print(f"Part 1: {min([sum(list(map(lambda x: abs(x-pos), crabs))) for pos in range(min(crabs), max(crabs)+1)])}")
print(f"Part 2: {min([sum(list(map(lambda x: (abs(x-pos) * (abs(x-pos)+1) /2), crabs))) for pos in range(min(crabs), max(crabs)+1)])}")