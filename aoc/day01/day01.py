"""01: Sonar Sweep"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = [int(i) for i in self.input.splitlines()]

    def part_one(self) -> int:
        count = 0
        prev = self.input[0]
        for i in self.input[1:]:
            count += 1 if i > prev else 0
            prev = i
        return count

    def part_two(self) -> int:
        count = 0
        prev = self.input[0] + self.input[1] + self.input[2]
        for i in range(1, len(self.input) - 2):
            cur = self.input[i] + self.input[i + 1] + self.input[i + 2]
            count += 1 if cur > prev else 0
            prev = cur
        return count
