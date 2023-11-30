# You can copy/paste this template to start a new day

"""06: Lanternfish"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = [int(i) for i in self.input.split(',')]
        self.cache = {}

    def fish_count_down(self, state: int, days: int) -> int:
        if (state, days) in self.cache:
            return self.cache[(state, days)]

        fish_generated = []
        remaining_days = days
        while remaining_days >= 0:
            remaining_days -= state
            state = 7
            if remaining_days < 0:
                break
            fish_generated.append(remaining_days)
        count = len(fish_generated)
        for days_left_for_each_fish in fish_generated:
            count += self.fish_count_down(9, days_left_for_each_fish)
        self.cache[(state, days)] = count
        return count

    def part_one(self) -> int:
        count = len(self.input)
        for fish in self.input:
            count += self.fish_count_down(fish, 80 - 1)
        return count

    def part_two(self) -> int:
        count = len(self.input)
        """for fish in self.input:
            count += self.fish_count_down(fish, 256 - 1)"""
        return count
