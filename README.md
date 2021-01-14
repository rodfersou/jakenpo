# jakenpo

Simple implementation of Rock Paper Scissors game

```python
from jakenpo import Choice, Match

match = Match()

print("Round 1   =>   (ROCK,    PAPER  )   =>  ", match.round(Choice.ROCK, Choice.PAPER))
print("Round 2   =>   (SCISSOR, PAPER  )   =>  ", match.round(Choice.SCISSOR, Choice.PAPER))
print("Round 3   =>   (ROCK,    SCISSOR)   =>  ", match.round(Choice.ROCK, Choice.SCISSOR))
print()
print(f"Winner in {match.rounds} rounds: {match.winner}")
```

```
Round 1   =>   (ROCK,    PAPER  )   =>   PLAYER2
Round 2   =>   (SCISSOR, PAPER  )   =>   PLAYER1
Round 3   =>   (ROCK,    SCISSOR)   =>   PLAYER1

Winner in 3 rounds: PLAYER1
```
