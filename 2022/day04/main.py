

def get_data(path: str = "./input.txt") -> list[str]:
    with open(path, "r") as data_file:
        return list(map(lambda s: s.strip(), data_file.readlines()))


def get_range(pair: str) -> range:
    start, stop = pair.split("-")
    return range(int(start), int(stop) + 1)


def parse_line(line: str) -> tuple[range, range]:
    r1, r2 = line.split(",")
    return get_range(r1), get_range(r2)


def solution(data: list[str]) -> tuple[int, int]:
    subsets_sum = 0
    overlapping_sum = 0
    for line in data:
        range1, range2 = parse_line(line)
        if all(el in range2 for el in range1) or all(el in range1 for el in range2):
            subsets_sum += 1
        if any(el in range2 for el in range1) or any(el in range1 for el in range2):
            overlapping_sum += 1

    return subsets_sum, overlapping_sum


if __name__ == "__main__":
    part1, part2 = solution(get_data())
    print("--- DAY 4 SOLUTIONS ---")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
