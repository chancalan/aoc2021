# You can copy/paste this template to start a new day

"""07: The Treachery of Whales"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = sorted([int(i) for i in self.input.split(",")])
        self.cache = [0 for _ in range(2000)]
        self.cache[0] = 1
        self.last_seen = 1

    def calculate_fuel_need(self, num: int):
        if self.cache[num - 1] != 0:
            return self.cache[num - 1]

        result = self.cache[self.last_seen - 1]
        for i in range(self.last_seen + 1, num + 1):
            result += i
            self.cache[i - 1] = result
        self.last_seen = num
        return result

    def part_one(self) -> int:
        result = float("inf")
        for i in range(self.input[0], self.input[-1] + 1):
            temp = 0
            for crab_pos in self.input:
                temp += abs(crab_pos - i)
            result = min(result, temp)
        return result

    def part_two(self) -> int:
        result = float("inf")
        for i in range(self.input[0], self.input[-1] + 1):
            temp = 0
            for crab_pos in self.input:
                temp += self.calculate_fuel_need(abs(crab_pos - i))
            result = min(result, temp)

        return result
