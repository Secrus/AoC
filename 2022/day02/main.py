shape_to_score_map = {
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


def calc_scores(data: list[tuple[int, int]]) -> tuple[int, int]:
    score_1 = 0
    score_2 = 0
    for o, m in data:
        if o == ROCK:
            score_1 += m
            if m == ROCK:
                score_1 += DRAW
                score_2 += 3
            elif m == PAPER:
                score_1 += WIN
                score_2 += (DRAW + 1)
            elif m == SCISSORS:
                score_2 += (WIN + 2)
        elif o == PAPER:
            score_1 += m
            if m == ROCK:
                score_2 += 1
            elif m == PAPER:
                score_1 += DRAW
                score_2 += (DRAW + 2)
            elif m == SCISSORS:
                score_1 += WIN
                score_2 += (WIN + 3)
        elif SCISSORS:
            score_1 += m
            if m == ROCK:
                score_1 += WIN
                score_2 += 2
            elif m == PAPER:
                score_2 += (DRAW + 3)
            elif m == SCISSORS:
                score_1 += DRAW
                score_2 += (WIN + 1)
    return score_1, score_2


def solution(data: list[str]) -> tuple[int, int]:
    return calc_scores(normalize_data(data))


if __name__ == "__main__":
    part1, part2 = solution(get_data())
    print("--- DAY 2 SOLUTIONS ---")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

