## Logging example
import logging

## Basic setup for logging
logging.basicConfig(filename='Python_Programming/logging/loggingExample1.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG) ## Turn off debug logging at critical level or lower

##### Log Levels #####
## debug - Lowest level
## info
## warning
## error
## critical - Highest Level
## Up to user to determine what level to log at

logging.debug('Start of program')

## Buggy Factorial code
def factorial(n):
    logging.debug('Start of factorial({0})'.format(n))
    total = 1
    for i in range (1,n + 1):
        total *= i
        logging.info('i: {0}, total: {1}'.format(i,total))
    logging.debug('Return value: {0}'.format(total))
    return total

print(factorial(5))

logging.debug('End of program')