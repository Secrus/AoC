

shape_to_score_map ={
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3
}
ROCK = 1
PAPER = 2
SCISSORS = 3
DRAW = 3
WIN = 6

def get_data(path: str = "./input.txt") -> list[str]:
    with open(path, "r") as data_file:
        return list(map(lambda s: s.strip(), data_file.readlines()))


def normalize_data(data: list[str]) -> list[tuple[int, int]]:
    tupled = list(map(lambda x: tuple(x.split(" ")), data))
    return [(shape_to_score_map[o], shape_to_score_map[m]) for o, m in tupled]


def calc_score_part1(data: list[tuple[int, int]]) -> int:
    score = 0
    for o, m in data:
        if o == ROCK:
            score += m
            if m == ROCK:
                score += DRAW
            elif m == PAPER:
                score += WIN
            elif m == SCISSORS:
                ...
        elif o == PAPER:
            score += m
            if m == ROCK:
                ...
            elif m == PAPER:
                score += DRAW
            elif m == SCISSORS:
                score += WIN

        elif SCISSORS:
            score += m
            if m == ROCK:
                score += WIN
            elif m == PAPER:
                ...
            elif m == SCISSORS:
                score += DRAW
    return score


def calc_score_part2(data: list[tuple[int, int]]) -> int:
    score = 0
    for o, m in data:
        if o == ROCK:
            if m == 1: # LOOSE
                score += 3
            elif m == 2: # DRAW
                score += (3 + 1)
            elif m == 3: # WIN
                score += (6 + 2)
        elif o == PAPER:
            if m == 1:
                score += 1
            elif m == 2:
                score += (3 + 2)
            elif m == 3:  # WIN
                score += (6 + 3)
        elif o == SCISSORS:
            if m == 1:
                score += 2
            elif m == 2:
                score += (3 + 3)
            elif m == 3:  # WIN
                score += (6 + 1)

    return score


def solution(data: list[str]) -> tuple[int, int]:
    part1 = calc_score_part1(normalize_data(data))
    part2 = calc_score_part2(normalize_data(data))
    return part1, part2


if __name__ == "__main__":
    part1, part2 = solution(get_data())
    print("--- DAY 2 SOLUTIONS ")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

