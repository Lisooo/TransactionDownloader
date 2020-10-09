import os
import datetime


class DatabaseParams(object):
    CxOracleHomeBudgeConnectionString = os.environ.get('CxOracleHomeBudgetConnectionString')


class PageParams(object):
    login_page_lnk = "https://www.ipko.pl/login.html"


class LoginParams(object):

    username = os.environ.get('IpkoUser')
    password = os.environ.get('IpkoPass')


class DateParams(object):
    start_dt = datetime.date(year=2019, month=1, day=1)
    current_dt = datetime.date.today()
    current_dttm = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


class FileParams(object):
    files_dir = os.environ.get('CsvFilesDir')
    logs_dir = "logs/"
    file_format = "'CSV'"
