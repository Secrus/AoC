

with open("input.txt", "r") as input_file:
    lines = map(lambda x: tuple(x.split()), input_file.readlines())

def solution(lines):
    depth = 0 
    forward = 0
    aim = 0
    for direction, value in lines:
        # pattern matching works on python >= 3.10
        match(direction):
            case "forward":
                forward += int(value)
                aim += depth * int(value)
            case "up":
                depth -= int(value)
            case "down":
                depth += int(value)

    return (forward * depth, forward * aim)



part1 , part2 = solution(lines)
print(f"PART 1: {part1}")
print(f"PART 2: {part2}")

