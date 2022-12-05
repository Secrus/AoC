import re


def initial_state() -> list[list[str]]:
    """
                            [R] [J] [W]
                [R] [N]     [T] [T] [C]
    [R]         [P] [G]     [J] [P] [T]
    [Q]     [C] [M] [V]     [F] [F] [H]
    [G] [P] [M] [S] [Z]     [Z] [C] [Q]
    [P] [C] [P] [Q] [J] [J] [P] [H] [Z]
    [C] [T] [H] [T] [H] [P] [G] [L] [V]
    [F] [W] [B] [L] [P] [D] [L] [N] [G]
     1   2   3   4   5   6   7   8   9
    """
    return [
        ["F", "C", "P", "G", "Q", "R"],
        ["W", "T", "C", "P"],
        ["B", "H", "P", "M", "C"],
        ["L", "T", "Q", "S", "M", "P", "R"],
        ["P", "H", "J", "Z", "V", "G", "N"],
        ["D", "P", "J"],
        ["L", "G", "P", "Z", "F", "J", "T", "R"],
        ["N", "L", "H", "C", "F", "P", "T", "J"],
        ["G", "V", "Z", "Q", "H", "T", "C", "W"],
    ]


def get_data(path: str = "./input.txt") -> list[str]:
    with open(path, "r") as data_file:
        return list(map(lambda s: s.strip(), data_file.readlines()))


def parse_commands(commands: list[str]) -> list[tuple[int, ...]]:
    return [
        tuple(map(int, re.findall(r"\d+", command))) for command in commands
    ]

def part_2(commands: list[str]) -> str:
    stacks = initial_state()
    for move, from_, to in parse_commands(commands):
        els = []
        from_ -= 1
        to -= 1
        for i in range(move):
            els.append(stacks[from_].pop())
        els.reverse()
        stacks[to].extend(els)

    return "".join([l[-1] for l in stacks])


def part_1(commands: list[str]) -> str:
    stacks = initial_state()
    for move, from_, to in parse_commands(commands):
        from_ -= 1
        to -= 1
        for i in range(move):
            el = stacks[from_].pop()
            stacks[to].append(el)

    return "".join([l[-1] for l in stacks])


def solution(data: list[str]) -> tuple[str, str]:

    return part_1(data), part_2(data)

if __name__ == "__main__":
    part1, part2 = solution(get_data())
    print("--- DAY 4 SOLUTIONS ---")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")