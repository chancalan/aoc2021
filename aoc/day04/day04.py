# You can copy/paste this template to start a new day

"""04: Giant Squid"""
import aoc.util
import re
from typing import List, Set, Tuple


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
        self.part1 = 0
        self.part2 = 0
        self.bingo_on_card = [False for _ in range(self.num_cards)]
        # solution() will find the answers for both parts
        self.solution()

    def parse_input(self) -> None:
        """
        parse self.input into self.num_drawn and self.cards
        Input: None
        Output: None
        """
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

    def find_num_in_all_cards(self, target: int) -> None:
        """
        Go through each bingo cards to look for target
        and mark self.bingo_tracker if found
        Input: target
        Output: None
        Note: If a bingo is already found in a certain card, we skip looking for target in that card
        """
        for i, card in enumerate(self.cards):
            if self.bingo_on_card[i]:
                continue
            num_found, r, c = self.find_num_in_card(card, target)
            if not num_found:
                continue
            self.bingo_tracker[i][0][r] = self.bingo_tracker[i][0][r] | self.bitmasks[c]
            self.bingo_tracker[i][1][c] = self.bingo_tracker[i][1][c] | self.bitmasks[r]

    def find_num_in_card(self, card: List[List[int]], target: int) -> Tuple[bool, int, int]:
        """
        Input: Given a bingo card, find the targeted num in it
        Output: a tuple where
                1) True, if target found, else False
                2) if #1 is True, row index of where target is, otherwise None
                3) if #1 is True, column index of where target is, otherwise None
        """
        for r, line in enumerate(card):
            for c, num in enumerate(line):
                if num == target:
                    return (True, r, c)
        return (False, None, None)

    def check_for_bingo(self) -> Tuple[bool, int]:
        """
        Input: None
        Output: A tuple where
                1) True, when found the first bingo, else False,
                2) if #1 is True, card index that bingo reside, else None
        """
        for i, card in enumerate(self.bingo_tracker):
            for r, row_status in enumerate(card[0]):
                if row_status == self.bingo_num:
                    return (True, i)
            for c, col_status in enumerate(card[1]):
                if col_status == self.bingo_num:
                    return (True, i)
        return (False, None)

    def check_for_bingo_without_returning_on_first(self) -> Set[int]:
        """
        Input: None
        Output: A set of cards that have bingo
        Note: we are skipping on cards that bingo were found on them already
        """
        result = set()
        for i, card in enumerate(self.bingo_tracker):
            if self.bingo_on_card[i]:
                continue
            for r, row_status in enumerate(card[0]):
                if row_status == self.bingo_num:
                    result.add(i)
            for c, col_status in enumerate(card[1]):
                if col_status == self.bingo_num:
                    result.add(i)
        return result

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

    def solution(self):
        """
        Find the answer to both parts of this problem
        """
        # don't need to do a bingo check for the first 5 draw
        j = 0
        while j < 5:
            self.find_num_in_all_cards(self.nums_drawn[j])
            j += 1

        # find the first bingo for part 1
        while j < len(self.nums_drawn):
            self.find_num_in_all_cards(self.nums_drawn[j])
            bingo_found, card_num = self.check_for_bingo()
            if bingo_found:
                self.bingo_on_card[card_num] = True
                self.part1 = self.get_unmarked_sum(card_num) * self.nums_drawn[j]
                j += 1
                break
            j += 1

        # find the last bingo card for part 2
        for num in self.nums_drawn[j:]:
            self.find_num_in_all_cards(num)
            bingo_found = self.check_for_bingo_without_returning_on_first()
            for card_num in bingo_found:
                self.bingo_on_card[card_num] = True
            if all(self.bingo_on_card):
                break
        else:
            raise ("Not all cards have bingo, something is wrong")

        # based on the problem statement, the last bingo found can only be in one card
        if len(bingo_found) != 1:
            raise ("Multiple bingo cards were found as the last bingo, something is wrong")

        self.part2 = self.get_unmarked_sum(list(bingo_found)[0]) * num

    def part_one(self) -> int:
        return self.part1

    def part_two(self) -> int:
        return self.part2
