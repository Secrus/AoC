from collections import Counter


def vectored_range(a, b):
    return range(a, b + 1) if a <= b else range(a, b - 1, -1)


def parse(transition: list[str]):
    x1, rest = transition.split(",", 1)
    y1, rest = rest.split("->")
    x2, y2 = rest.split(",")
    x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])

    straight = []
    diagonal = []

    if (x1 == x2) or (y1 == y2):
        for i in vectored_range(x1, x2):
            for j in vectored_range(y1, y2):
                straight.append((i, j))
    else:
        for point in zip(vectored_range(x1, x2), vectored_range(y1, y2)):
            diagonal.append(point)
    return straight, diagonal


with open("input.txt", "r") as input_file:
    transitions = list(map(lambda x: x.strip(), input_file.readlines()))

straight = []
diagonal = []

for coords in transitions:
    st, diag = parse(coords)
    straight.extend(st)
    diagonal.extend(diag)

part_1 = len(list(filter(lambda x: x > 1, dict(Counter(straight)).values())))
straight.extend(diagonal)
part_2 = len(list(filter(lambda x: x > 1, dict(Counter(straight)).values())))

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
