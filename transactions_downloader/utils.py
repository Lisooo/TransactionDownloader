from transactions_downloader.dictionaries.dictDateTime import DictDatetime

import datetime
import time


class DateUtils(object):

    @staticmethod
    def get_variables_from_date(v_date):
        if type(v_date) is str:
            year = v_date[0:4]  # YYYY
            month = v_date[5:7]  # MM
            day = v_date[8:10]  # DD
        else:
            print("błędny typ daty")
            quit()

        return day, month, year

    @staticmethod
    def set_variables_to_date(day, month, year):
        date = datetime.date(int(year), int(month), int(day))
        return date

    @staticmethod
    def get_day_from_date(v_date):
        return int(v_date[1:2])

    @staticmethod
    def get_month_from_date(v_date):
        return int(v_date[3:5])

    @staticmethod
    def get_year_from_date(v_date):
        return int(v_date[6:10])

    @staticmethod
    def add_days_to_date(v_date, x):
        new_date = v_date + datetime.timedelta(days=x)
        return new_date

    @staticmethod
    def date_to_string(v_date):
        v_date = str(v_date).replace("-", '').replace(".", '')
        return v_date

    @staticmethod
    def get_month_name_from_dict(v_month_nb):
        month_nm = DictDatetime.dict_moth(v_month_nb)
        return month_nm


class TimeUtils(object):

    @staticmethod
    def wait_x_sec(x):
        time.sleep(x)

