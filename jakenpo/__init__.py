from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, unique
from typing import DefaultDict


@unique
class Winner(Enum):
    PLAYER1 = "PLAYER1"
    PLAYER2 = "PLAYER2"
    DEUCE   = "DEUCE"


@unique
class Choice(Enum):
    ROCK    = "ROCK"
    PAPER   = "PAPER"
    SCISSOR = "SCISSOR"


GAME_MAPPING = {
    Choice.ROCK: {
        Choice.SCISSOR: Winner.PLAYER1,
        Choice.ROCK: Winner.DEUCE,
        Choice.PAPER: Winner.PLAYER2,
    },
    Choice.PAPER: {
        Choice.ROCK: Winner.PLAYER1,
        Choice.PAPER: Winner.DEUCE,
        Choice.SCISSOR: Winner.PLAYER2,
    },
    Choice.SCISSOR: {
        Choice.PAPER: Winner.PLAYER1,
        Choice.SCISSOR: Winner.DEUCE,
        Choice.ROCK: Winner.PLAYER2,
    },
}


@dataclass
class Match:
    rounds: int = 0
    matches: DefaultDict[Winner, int] = field(default_factory=lambda: defaultdict(int))

    def round(self, choice_player1: Choice, choice_player2: Choice) -> str:
        winner = GAME_MAPPING[choice_player1][choice_player2]

        self.rounds += 1
        self.matches[winner] += 1

        return winner.value

    @property
    def winner(self) -> str:
        if self.matches[Winner.PLAYER1] > self.matches[Winner.PLAYER2]:
            return Winner.PLAYER1
        elif self.matches[Winner.PLAYER1] < self.matches[Winner.PLAYER2]:
            return Winner.PLAYER2
        else:
            return Winner.DEUCE


if __name__ == "__main__":
    match = Match()

    print("Round 1   =>   (ROCK,    PAPER  )   =>  ", match.round(Choice.ROCK, Choice.PAPER))
    print("Round 2   =>   (SCISSOR, PAPER  )   =>  ", match.round(Choice.SCISSOR, Choice.PAPER))
    print("Round 3   =>   (ROCK,    SCISSOR)   =>  ", match.round(Choice.ROCK, Choice.SCISSOR))
    print()
    print(f"Winner in {match.rounds} rounds: {match.winner}")
