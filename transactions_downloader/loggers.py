import logging
from transactions_downloader.params import FileParams
import datetime


class Logger(object):

    def __init__(self, name):
        self.name = name
        self.datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s: %(message)s', "%Y-%m-%d %H:%M:%S")

        self.file_handler = logging.FileHandler(f'{FileParams.logs_dir}/log_{self.datetime}.log')
        self.file_handler.setFormatter(formatter)

    def logger(self):
        logger = logging.getLogger(self.name)
        logger.addHandler(self.file_handler)
        logger.setLevel(logging.INFO)
        logger.isEnabledFor(logging.WARNING)
        logger.isEnabledFor(logging.ERROR)
        return logger
