# You can copy/paste this template to start a new day

"""05: Hydrothermal Venture"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.parse_input()
        # call calculating_paths_*() to get part1 and part2 solution
        self.seen = set()
        self.more_than_2 = set()
        self.part2list = []
        self.part1 = 0
        self.part2 = 0
        self.calculating_paths_part1()
        self.calculating_paths_part2()

    def parse_input(self) -> None:
        """
        self.input will turn into a list of list of start and end points
        """
        self.input = self.input.splitlines()
        self.input = [item.split(" -> ") for item in self.input]

    def calculating_paths_part1(self) -> None:
        """
        calculate paths for the horizontal and vertical lines
        put the diagonal lines in self.part2list
        """
        for toandfrom in self.input:
            start = [int(i) for i in toandfrom[0].split(",")]
            end = [int(i) for i in toandfrom[1].split(",")]
            if start[0] == end[0] or start[1] == end[1]:  # for part 1
                item = tuple(start)
                if item in self.seen:
                    self.more_than_2.add(item)
                else:
                    self.seen.add(item)
                while start[0] != end[0] or start[1] != end[1]:
                    if start[0] < end[0]:
                        start[0] += 1
                    elif start[0] > end[0]:
                        start[0] -= 1

                    if start[1] < end[1]:
                        start[1] += 1
                    elif start[1] > end[1]:
                        start[1] -= 1

                    key = tuple(start)
                    if key in self.seen:
                        self.more_than_2.add(key)
                    else:
                        self.seen.add(key)
            else:  # getting ready for diagonal for part 2
                self.part2list.append([start, end])

        self.part1 = len(self.more_than_2)

    def calculating_paths_part2(self):
        """
        calculating paths for diagonal lines
        which they are in self.part2list generated from calculating_paths_part1()
        """
        for start, end in self.part2list:
            item = tuple(start)
            if item in self.seen:
                self.more_than_2.add(item)
            else:
                self.seen.add(item)
            # assuming they are 45degree diagonal, this check is good enough
            while start[0] != end[0]:
                if start[0] < end[0]:
                    start[0] += 1
                elif start[0] > end[0]:
                    start[0] -= 1

                if start[1] < end[1]:
                    start[1] += 1
                elif start[1] > end[1]:
                    start[1] -= 1

                key = tuple(start)
                if key in self.seen:
                    self.more_than_2.add(key)
                else:
                    self.seen.add(key)
            self.part2 = len(self.more_than_2)

    def part_one(self) -> int:
        return self.part1

    def part_two(self) -> int:
        return self.part2
