import random

def show_word(word,pos,example):
    print(f'{word}\n'+'-'*30+f'\nPOS: {pos}\ne.g.\n{example}\n')

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second