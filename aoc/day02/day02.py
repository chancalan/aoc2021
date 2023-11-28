# You can copy/paste this template to start a new day

"""02: Dive!"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = self.input.splitlines()

    def part_one(self) -> int:
        h = d = 0
        for line in self.input:
            direction, unit = line.split(" ")
            if direction == "forward":
                h += int(unit)
            elif direction == "down":
                d += int(unit)
            else:  # direciton == 'up'
                d -= int(unit)
        return h * d

    def part_two(self) -> int:
        aim = h = d = 0
        for line in self.input:
            direction, unit = line.split(" ")
            if direction == "down":
                aim += int(unit)
            elif direction == "up":
                aim -= int(unit)
            else:  # direction == forward
                unit = int(unit)
                h += unit
                d += aim * unit
        return h * d
