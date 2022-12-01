import itertools

with open("input.txt", "r") as input_file:
    lines = list(map(int, input_file.readlines()))


def sum_pairwise_increases(x):
    # itertools.pairwise works with python >= 3.10
    return sum([1 if a < b else 0 for a, b in itertools.pairwise(x)])


print(f"Part 1: {sum_pairwise_increases(lines)}")
print(
    f"Part 2: {sum_pairwise_increases([sum(lines[i:i+3]) for i in range(len(lines)-2)])}"
)
