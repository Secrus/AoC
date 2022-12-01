class Board:
    def __init__(self, board_str):
        self.numbers = [int(s) for s in board_str.split()]
        self.left = set(self.numbers)

    @property
    def won(self):
        for i in range(5):
            for j in range(5):
                if self.numbers[i * 5 + j] in self.left:
                    break
            else:
                return True

            for j in range(5):
                if self.numbers[i + j * 5] in self.left:
                    break
            else:
                return True
        else:
            return False


def calculate():
    with open("input.txt", "r") as input_file:
        calls, *matrixes = input_file.read().split("\n\n")

    boards = [Board(s) for s in matrixes]

    first_won = None
    last_won = -1
    seen = set()
    for number in (int(s) for s in calls.split(",")):
        for board in boards:
            board.left.discard(number)

        for i, board in enumerate(boards):
            if i not in seen and board.won:
                value = sum(board.left) * number
                if first_won is None:
                    first_won = value
                last_won = value
                seen.add(i)
    return first_won, last_won


part1, part2 = calculate()
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
