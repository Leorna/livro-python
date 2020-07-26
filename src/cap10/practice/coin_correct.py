import random

coin = { 'heads': 0, 'tails': 1 }
guess = ''

while guess not in coin.keys():
    print('Guess the coin toss!')
    guess = input('Enter heads or tails: ').lower()


toss = random.randint(0, 1)

if toss == coin[guess]:
    print('You got it!')
else:
    guess = input('Nope! Guess again: ').lower()
    if toss == coin[guess]:
        print('You got it!')
    else:
        print('Nope! You are really bad at this game.')
