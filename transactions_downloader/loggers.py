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


# logger = Logger.logger()
# logging.basicConfig(filename=f'logs/{logger.name}.log', level=logging.INFO)

#
# class ImportLog(object):
#
#     def __init__(self, cursor):
#         self.table_nm = "Import_log"
#         self.cursor = cursor
#
#         self.files_dir = FileUtils().get_files_list_from_dir()
#         self.start_dt = datetime.date(year=2019, month=1, day=1)
#         self.current_dt = datetime.date.today()
#         self.current_dttm = datetime.datetime.today()
#
#         logger.info(f'Created ImportLog Instance with params: '
#                     f'\n- start_dt {self.start_dt} '
#                     f'\n- current_dt {self.current_dt} '
#                     f'\n- current_dttm {self.current_dttm}')

# def my_logger(orig_func):
#     logging.basicConfig(filename=f'logs/{orig_func.__name__}.log', level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         logging.info(f' [{datetime.datetime.today()}] Ran with args: {args}, and kwargs: {kwargs}')
#         return orig_func(*args, **kwargs)
#
#     return wrapper
