#! python3.8

import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


guess = ''

logging.debug('Start of program')
logging.debug(f'guess is {guess}')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss!')
    guess = input('Enter heads or tails: ')
    logging.debug(f'guess is {guess}')

toss = random.randint(0, 1) # tails is 0, heads is 1
logging.debug(f'toss is {toss}')

logging.debug('Comparing guess == toss')
if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again: ')
    logging.debug(f'guess is {guess}')
    logging.debug(f'toss is {toss}')
    logging.debug('Comparing guess == toss')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! You are really bad at this game.')

logging.debug('End of program')