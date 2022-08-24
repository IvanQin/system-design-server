from abc import staticmethod
import logging

class Logger():

    logging.basicConfig(level=logging.DEBUG, format='%(process)d-%(levelname)s-%(message)s')

    @staticmethod
    def i(tag: str, msg : str):
        logging.info(f'[{tag}] {msg}')
