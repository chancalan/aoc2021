# You can copy/paste this template to start a new day

"""06: Lanternfish"""
import aoc.util
from collections import Counter


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = [int(i) for i in self.input.split(",")]
        self.cache = {}

    def fish_count_down_dfs_approach(self, state: int, days: int) -> int:
        """
        Input: take the state of a fish as int and days left as int
        Output: total of fish reproduced by the given fish
        Example: self.fish_count_down_dfs_approach(3, 80 - 1)
        for a fish that will reproduce in 3 days with 80 days left
        """
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
            count += self.fish_count_down_dfs_approach(9, days_left_for_each_fish)
        self.cache[(state, days)] = count
        return count

    def fish_counting(self, days: int) -> int:
        """
        Input: number of days left as int
        Output: the total number of fish exists after the given days
        using self.input as input
        """
        fishes = Counter({i: 0 for i in range(9)})
        fishes.update(Counter(self.input))
        for _ in range(days):
            zeros = fishes[0]
            for i in range(1, len(fishes)):
                fishes[i - 1] = fishes[i]
                fishes[i] = 0

            fishes[6] += zeros
            fishes[8] += zeros
        return fishes.total()

    def part_one(self) -> int:
        return self.fish_counting(80)

    def part_two(self) -> int:
        return self.fish_counting(256)
