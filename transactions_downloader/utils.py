from transactions_downloader import db
from transactions_downloader.dictionaries.dictDateTime import DictDatetime
from transactions_downloader.models import ImportLog

import datetime
import time
import os


class DateUtils(object):

    @staticmethod
    def get_variables_from_str_date(str_date):
        year = str_date[0:4]  # YYYY
        month = str_date[4:6]  # MM
        day = str_date[6:8]  # DD

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


class FileUtils(object):

    @staticmethod
    def get_files_list_from_dir(v_dir):
        v_file_list = os.listdir(v_dir)  # list of files in directory
        return v_file_list

    @staticmethod
    def find_latest_file_nm(v_dir):
        filename = max([f for f in os.listdir(v_dir)],
                       key=lambda xa: os.path.getctime(os.path.join(v_dir, xa)))
        return filename

    @staticmethod
    def file_nm_into_str_date(file_nm):
        file = file_nm.replace("history_csv_", "")
        file = file[0:8]
        return file

    @staticmethod
    def set_filepath(v_dir, v_file_nm):
        file_nm_path = os.path.join(v_dir, v_file_nm)
        return file_nm_path

    @staticmethod
    def change_file_nm(v_old_file_nm, v_new_file_nm):
        os.rename(v_old_file_nm, v_new_file_nm)
        print("File name was changed from: " + v_old_file_nm + " to " + v_new_file_nm)

    @staticmethod
    def add_file_nm_to_list(v_file_nm, v_list):
        v_file_nm = str(v_file_nm)
        v_list.append(v_file_nm)

    @staticmethod
    def generate_date_list_to_download(v_start_dt, p_curr_dttm, v_file_list):
        v_dt_list = []
        v_import_csv_dt = DBUtils.import_log_dates_into_list()  # list of dates in IMPORT CSV log
        v_final_dt_list = []
        v_curr_dt = p_curr_dttm.date()

        for file_nm in v_file_list:
            v_file_nm = str(file_nm)
            v_dt_list.append(v_file_nm)

        while v_start_dt < v_curr_dt:
            v_date = str(v_start_dt).replace("-", '').replace(".", '')
            v_file_date = v_start_dt + datetime.timedelta(days=1)
            v_file_date = str(v_file_date).replace("-", '').replace(".", '')

            if str(v_file_date) in str(v_dt_list):
                print(v_date + ": there is a file with transactions")
                pass
            elif v_date in v_import_csv_dt:
                print(v_date + ": exists in IMPORT CSV log (probably no transactions on that day)")
                pass
            else:
                print(v_date + ": added into download date list")
                v_final_dt_list.append(v_date)

            v_start_dt = v_start_dt + datetime.timedelta(days=1)

        return v_final_dt_list


class DBUtils(object):

    @staticmethod
    def import_log_dates_into_list():
        rslt = ImportLog.query.order_by(ImportLog.operation_dt).all()
        db_date_list = []
        for row in rslt:
            row.operation_dt = str(row.operation_dt).replace("-", '').replace(".", '')
            db_date_list.append(row.operation_dt)
        return db_date_list

    @staticmethod
    def insert_into_import_log(v_file_nm, v_oprtn_dt, v_download_dtm, v_download_msg, v_import_flg, v_etl_flg):
        # check if transaction date not in import csv log
        db_date_list = DBUtils.import_log_dates_into_list()

        if str(v_oprtn_dt) in db_date_list:
            print("Data transakcji: " + str(v_oprtn_dt) + " jest już w logu")
            pass
        else:
            new_id = db.session.query(
                db.func.max(ImportLog.file_id)).scalar()  # brak autoincrement dla ORACLE.

            if new_id is None:  # w przypadku pierwszego wpisu (pusta tabela)
                new_id = 1
            else:
                new_id = db.session.query(
                    db.func.max(ImportLog.file_id)).scalar() + 1

            new_import_log = ImportLog(file_id=new_id,
                                          file_nm=v_file_nm,
                                          operation_dt=v_oprtn_dt,
                                          download_dtm=v_download_dtm,
                                          download_msg=v_download_msg,
                                          import_flg=v_import_flg,
                                          etl_flg=v_etl_flg)
            db.session.add(new_import_log)
            db.session.commit()
