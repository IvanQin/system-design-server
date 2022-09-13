import logging

class Logger():

    logging.basicConfig(level=logging.DEBUG, format='%(process)d-%(levelname)s-%(message)s')

    @staticmethod
    def i(tag: str, msg : str):
        logging.info(f'INFO [{tag}] {msg}')

    @staticmethod
    def d(tag: str, msg : str):
        logging.info(f'DEBUG [{tag}] {msg}')
