# Hi!
## This is my "bigger" project in Python, hope u like it.
### Description
The project is contained in one .py file which, when exexuted, starts a game of chess in a terminal.

The printed board looks like that:
```
  +---+---+---+---+---+---+---+---+
8 | r | n | b | q | k | b | n | r |
  +---+---+---+---+---+---+---+---+
7 | p | p | p | p | p | p | p | p |
  +---+---+---+---+---+---+---+---+
6 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
2 | P | P | P | P | P | P | P | P |
  +---+---+---+---+---+---+---+---+
1 | R | N | B | Q | K | B | N | R |
  +---+---+---+---+---+---+---+---+
    a   b   c   d   e   f   g   h  
```

It's printed before each move and when the game ends (whether because it's a checkmate or a draw)

In each move you're asked to enter the square you want to move from - e.g. "e4" - and a square you want to move to - e.g. "e5".

If the move you're trying to make is illegal or you've typed something that isn't an existing square such as "e9" or "ilovechess" you'll be asked to enter your move again up to a point in which you enter a legal one.

The only features unavailable are automatic draws due to the 50 move rule, thhreefold repetition and impossibility of checkmate with each player having only one bishop, both of the same colour. I may add those features later.

Other feature that may be added at a later date include a cusomizable position you start from.

Thx for reading!
