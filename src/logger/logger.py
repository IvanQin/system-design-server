import logging

class Logger():

    logging.basicConfig(level=logging.DEBUG, format='%(process)d-%(levelname)s-%(message)s')

    @staticmethod
    def i(tag: str, action : str, msg : str):
        logging.info(f'INFO [{tag}][{action}] {msg}')
