# You can copy/paste this template to start a new day

"""04: Giant Squid"""
import aoc.util
import re
from typing import List, Tuple


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = self.input.splitlines()
        self.nums_drawn = []
        self.cards = []
        self.parse_input()
        self.num_cards = len(self.cards)
        self.bitmasks = [2**i for i in reversed(range(5))]
        self.bingo_tracker = [
            [[0 for _ in range(5)], [0 for _ in range(5)]]  # tracking rows  # tracking columns
            for _ in range(self.num_cards)
        ]
        self.bingo_num = 31

    def parse_input(self) -> None:
        # parse self.input into self.num_drawn and self.cards
        self.nums_drawn = [int(i) for i in self.input[0].split(",")]
        i = 2
        card = []
        while i < len(self.input):
            if len(self.input[i]) != 0:
                card.append([int(i) for i in re.findall(r"(\d+)\s*", self.input[i])])
            else:
                self.cards.append(card)
                card = []
            i += 1
        self.cards.append(card)

    def find_num_in_card(self, card: List[List[int]], target: int) -> Tuple[bool, int, int]:
        for r, line in enumerate(card):
            for c, num in enumerate(line):
                if num == target:
                    return (True, r, c)
        return (False, None, None)

    def check_for_bingo(self) -> Tuple[bool, int]:
        for i, card in enumerate(self.bingo_tracker):
            for r, row_status in enumerate(card[0]):
                if row_status == self.bingo_num:
                    return (True, i)
            for c, col_status in enumerate(card[1]):
                if col_status == self.bingo_num:
                    return (True, i)
        return (False, None)

    def get_unmarked_sum(self, card_index: int) -> int:
        result = 0
        card = self.cards[card_index]
        for r, line in enumerate(card):
            if self.bingo_tracker[card_index][0][r] == self.bingo_num:
                continue
            for c, num in enumerate(card[r]):
                if not self.bingo_tracker[card_index][0][r] & self.bitmasks[c]:
                    result += num
        return result

    def part_one(self) -> int:
        # don't need to do a bingo check for the first 5 draw
        for num in self.nums_drawn[:5]:
            for i, card in enumerate(self.cards):
                num_found, r, c = self.find_num_in_card(card, num)
                if not num_found:
                    continue
                self.bingo_tracker[i][0][r] = self.bingo_tracker[i][0][r] | self.bitmasks[c]
                self.bingo_tracker[i][1][c] = self.bingo_tracker[i][1][c] | self.bitmasks[r]

        for num in self.nums_drawn[5:]:
            for i, card in enumerate(self.cards):
                num_found, r, c = self.find_num_in_card(card, num)
                if not num_found:
                    continue
                self.bingo_tracker[i][0][r] = self.bingo_tracker[i][0][r] | self.bitmasks[c]
                self.bingo_tracker[i][1][c] = self.bingo_tracker[i][1][c] | self.bitmasks[r]
            bingo_found, card_num = self.check_for_bingo()
            if bingo_found:
                break

        return self.get_unmarked_sum(card_num) * num

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
