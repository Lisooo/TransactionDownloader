from transactions_downloader.files.utils import FileUtils
from transactions_downloader.loggers import Logger
from transactions_downloader.params import DateParams
import datetime

logger = Logger('Import_Log').logger()


class ImportLog(object):

    def __init__(self, cursor):
        self.table_nm = 'Import_log'
        self.cursor = cursor

        self.files_dir = FileUtils().get_files_list_from_dir()
        self.start_dt = DateParams.start_dt
        self.current_dt = DateParams.current_dt
        self.current_dttm = DateParams.current_dttm

        logger.info(f'Started with params:')
        logger.info(f'#Start_dt# {self.start_dt}, #Current_dt# {self.current_dt}, #Current_dttm# {self.current_dttm}')

    def import_log_dates_into_list(self):
        rslt = self.cursor.execute("Select to_char(operation_dt,'YYYY-MM-DD') from " + self.table_nm
                                   + " order by operation_dt asc").fetchall()

        db_date_list = []
        for row in rslt:
            db_date_list.append(row[0])
        return db_date_list

    def insert_into_import_log(self, v_file_nm, v_oprtn_dt, v_download_msg, v_import_flg, v_etl_flg):
        # check if transaction date not in import csv log
        if str(v_oprtn_dt) in self.import_log_dates_into_list():
            print("Data transakcji: " + str(v_oprtn_dt) + " jest już w logu")
            pass
        else:
            new_id = self.cursor.execute("SELECT max(nvl(file_id,0)) FROM " + self.table_nm + "").fetchone()

            if new_id == 0:  # in case of first record
                new_id = 1
            else:
                new_id = int(new_id[0]) + 1

            dict_values = {"new_id": new_id,
                           "file_nm": v_file_nm,
                           "oprtn_dt": v_oprtn_dt,
                           "download_dttm": self.current_dttm,
                           "download_msg": v_download_msg,
                           "import_flg": v_import_flg,
                           "etl_flg": v_etl_flg}

            v_sql = f"INSERT INTO {self.table_nm} VALUES (:file_id, :file_nm, :operation_dt" \
                f", :download_dttm, :download_msg, :import_flg, :etl_flg)"

            self.cursor.execute(v_sql, [dict_values['new_id'], dict_values['file_nm'], dict_values['oprtn_dt']
                                ,dict_values["download_dttm"], dict_values["download_msg"], dict_values["import_flg"]
                                ,dict_values["etl_flg"]])

            logger.info(f'Record added properly')

    def generate_date_list_to_download(self):
        v_dt_list = []
        v_import_csv_dt = self.import_log_dates_into_list()  # list of dates in IMPORT CSV log
        v_final_dt_list = []

        for file_nm in self.files_dir:
            v_file_nm = str(file_nm)
            v_dt_list.append(v_file_nm)

        while self.start_dt < self.current_dt:
            v_date = str(self.start_dt)
            v_file_date = self.start_dt + datetime.timedelta(days=1)
            v_file_date = str(v_file_date).replace("-", '').replace(".", '')

            if v_file_date in str(v_dt_list):
                # print(v_date + ": there is a file with transactions")
                pass
            elif v_date in v_import_csv_dt:
                # print(v_date + ": exists in IMPORT CSV log (probably no transactions on that day)")
                pass
            else:
                v_final_dt_list.append(v_date)
                logger.info(f"{v_date} added into download date list")

            self.start_dt = self.start_dt + datetime.timedelta(days=1)
        if len(v_final_dt_list) == 0:
            logger.info(f"Date list is empty")

        return v_final_dt_list
