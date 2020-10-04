import cx_Oracle
from transactions_downloader.params import DatabaseParams


class HomeBudgetConnection(object):
    def __init__(self):
        self.uri = DatabaseParams.CxOracleHomeBudgeConnectionString

    def set(self):
        return cx_Oracle.connect(self.uri, encoding='UTF-8')
