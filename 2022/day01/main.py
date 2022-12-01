from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal


def get_data(path: str = "./input.txt") -> list[str]:
    with open(path, "r") as data_file:
        return list(map(lambda s: s.strip(), data_file.readlines()))


def normalize_data(data: list[str]) -> list[int | str]:
    return [int(el) if el.isdigit() else "" for el in data]


def group_data(data: list[int | Literal[""]]) -> list[list[int]]:
    result = []
    temp = []
    for el in data:
        if el != "":
            temp.append(el)
        else:
            result.append(temp)
            temp = []
    return result


def get_sorted_sums(data: list[list[int]]) -> list[int]:
    sums = list(map(sum, data))
    return sorted(sums, reverse=True)


def solution(data: list[str]) -> tuple[int, int]:
    data = get_sorted_sums(group_data(normalize_data(data)))
    return data[0], sum(data[0:3])


if __name__ == "__main__":
    part1, part2 = solution(get_data())
    print("--- DAY 1 SOLUTIONS ")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

