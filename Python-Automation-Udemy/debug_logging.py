"""
Logging stuff example.

LOG LEVELS:
    DEBUG (lowest level)
    INFO
    WARNING
    ERROR
    CRITICAL (highest level)
"""

import logging  # Lets you display log messages.

# This will print:
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# This will write to file (wont display in screen):
logging.basicConfig(filename='to_delete/myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Here is how you disable logging all at once once we are done debugging.
# Just comment this out when you want to debug again.
# logging.disable(logging.CRITICAL)   # CRITICAL disables all, but you can pick and choose what to diable.
# logging.disable(logging.DEBUG)      # This will diable all the DEBUG logging.

logging.debug('Start of program.')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.critical('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program.')
