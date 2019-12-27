import sys

sentence = ''
while True:
    sentence = input('> ')
    if sentence != 'quit':
        print(sentence.title())
    else:
        break