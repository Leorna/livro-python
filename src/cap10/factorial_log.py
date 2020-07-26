#! python3.8

import logging
#logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='factorial_log.txt')


logging.debug('Start of program')


def factorial(n: int) -> int:
    logging.debug(f'Start of factorial({n})')
    total: int = 1

    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')

    logging.debug(f'End of factorial({n})')
    return total


print(factorial(5))

logging.debug('End of program')