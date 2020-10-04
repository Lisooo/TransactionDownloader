import os
import datetime


class DatabaseParams(object):
    CxOracleHomeBudgeConnectionString = os.environ.get('CxOracleHomeBudgetConnectionString')


class PageParams(object):
    login_page_lnk = "https://www.ipko.pl/login.html"


class LoginParams(object):

    username = os.environ.get('IpkoUser')
    password = os.environ.get('IpkoPass')


class FileParams(object):
    files_dir = os.environ.get('CsvFilesDir')
    file_format = "'CSV'"


class DatesParams(object):
    curr_datetime = datetime.datetime.today()   # current datetime
    start_dt = datetime.date(year=2019, month=1, day=1)     # setting start day for HomeBudget Project
