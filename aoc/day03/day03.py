# You can copy/paste this template to start a new day

"""03: Binary Diagnostic"""
import aoc.util
from typing import List


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = self.input.splitlines()
        self.input_as_int = [int(num, 2) for num in self.input]
        self.input_size = len(self.input)
        self.lineitem_size = len(self.input[0])
        # binary representation of a specific spot
        self.spots = [2**i for i in reversed(range(self.lineitem_size))]

    def part_one(self) -> int:
        counts = counts = [0 for _ in range(self.lineitem_size)]
        # count the ones for each spot
        for item in self.input_as_int:
            for i, num in enumerate(self.spots):
                # if num & item != 0, it will return 1 else 0
                counts[i] += 1 if num & item else 0

        half = self.input_size / 2
        gamma = 0
        epsilon = 0
        for i, num in enumerate(counts):
            if num > half:
                gamma = self.spots[i] | gamma
            else:
                epsilon = self.spots[i] | epsilon
        return gamma * epsilon

    def selector(self, numlist: List[int], checker: int, keep_common: bool) -> List[int]:
        result = []
        count = 0
        for item in numlist:
            count += 1 if checker & item else 0

        half = len(numlist) / 2
        if keep_common:
            for item in numlist:
                if count >= half:
                    if item & checker:
                        # 1 as criteria bit
                        result.append(item)
                else:
                    if not item & checker:
                        # 0 as criteria bit
                        result.append(item)
        else:
            for item in numlist:
                if count < half:
                    if item & checker:
                        result.append(item)
                else:
                    if not item & checker:
                        result.append(item)
        return result

    def part_two(self) -> int:
        oxygen = self.input_as_int
        for i in range(self.lineitem_size):
            if len(oxygen) == 1:
                break
            oxygen = self.selector(oxygen, self.spots[i], True)

        co2 = self.input_as_int
        for i in range(self.lineitem_size):
            if len(co2) == 1:
                break
            co2 = self.selector(co2, self.spots[i], False)

        return oxygen[0] * co2[0]
