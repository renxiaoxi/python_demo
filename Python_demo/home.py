from Universe.util import show_word,Dice
from pathlib import Path

# show_word('good','adjective','She is a good engineer')

# dice = Dice()
# print(dice.roll())

path = Path()
for item in path.glob('*.*'):
    print(item)