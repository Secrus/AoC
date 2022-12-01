import copy


with open("input.txt", "r") as input_file:
    data = list(map(int, input_file.read().strip().split(",")))


def calculate_amount_of_fish(data, epochs):
    fish = 7 * [0]

    for entry in data:
        fish[entry] += 1

    sevens = 0
    eights = 0
    for i in range(epochs):
        m = fish[0]
        fish = fish[1:] + fish[:1]
        fish[6] += sevens
        sevens = eights
        eights = m

    return sum(fish) + sevens + eights


print(f"Part 1: {calculate_amount_of_fish(data, 80)}")
print(f"Part 2: {calculate_amount_of_fish(data, 256)}")
