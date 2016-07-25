import logging

logging.basicConfig(filename='my_program_log.txt', level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

logging.disable(logging.ERROR)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
