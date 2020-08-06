import os
import datetime


class Config:

    # FLASK PARAMS
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # LOGIN PARAMS
    USERNAME = os.environ.get('IPKOUSER')
    PASS = os.environ.get('IPKOPASS')

    # PAGE PARAMS
    SITE_URL = "https://www.ipko.pl/login.html"

    # CSV PARAMS
    CSV_FILES_DIR = os.environ.get('CSV_FILES_DIR')
    CSV_FILE_FORMAT = "'CSV'"

    # DATES PARAMS
    CURR_DATETIME = datetime.datetime.today()  # current date
    START_DT = datetime.date(year=2019, month=1, day=1)    # setting start_day of HomeBudget Project
