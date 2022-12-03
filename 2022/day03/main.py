import string
from more_itertools import chunked

def get_data(path: str = "./input.txt") -> list[str]:
    with open(path, "r") as data_file:
        return list(map(lambda s: s.strip(), data_file.readlines()))


def get_weight(char: str) -> int:
    if char in string.ascii_lowercase:
        return string.ascii_lowercase.index(char) + 1
    else:
        return string.ascii_uppercase.index(char) + 27


def split_list(items: str) -> tuple[str, str]:
    return items[:len(items)//2], items[len(items)//2:]


def solution(data: list[str]) -> tuple[int, int]:
    sum_of_most_common = 0
    for rucksack in data:
        comp_1, comp_2 = split_list(rucksack)
        common = set(comp_1) & set(comp_2)
        sum_of_most_common += get_weight(common.pop())

    sum_of_group_badges = 0
    for group in chunked(data, 3):
        badge = set(group[0]) & set(group[1]) & set(group[2])
        sum_of_group_badges += get_weight(badge.pop())

    return sum_of_most_common, sum_of_group_badges


if __name__ == "__main__":
    part1, part2 = solution(get_data())
    print("--- DAY 3 SOLUTIONS ---")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
