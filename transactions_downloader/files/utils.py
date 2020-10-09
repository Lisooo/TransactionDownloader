import os
from transactions_downloader.utils import DateUtils
from transactions_downloader.params import FileParams
from transactions_downloader.loggers import Logger

file_log = Logger('File').logger()


class FileUtils(object):

    def __init__(self, file_nm=None):
        self.dir = FileParams.files_dir

        if file_nm:
            # get provided file_nm
            self.file_nm = file_nm
        else:
            # get latest (recently downloaded) file_nm
            self.file_nm = max([f for f in os.listdir(self.dir)],
                                   key=lambda xa: os.path.getctime(os.path.join(self.dir, xa)))

        self.file_dt = self.file_nm.replace('history_csv_', '')[0:8]
        self.file_path = os.path.join(self.dir, self.file_nm)
        self.new_file_dt = ''

        file_log.info(f'Started with params:')
        file_log.info(f'#File_nm# {self.file_nm}')

    def get_files_list_from_dir(self):
        return os.listdir(self.dir)  # list of files in directory

    def set_new_file_dt(self, v_date):
        # 1. from <str> date ('YYYY-MM-DD'), get values: day, month, year
        # 2. from day, month, year generate <date> date
        # 3. add one day to <date> date
        # 4. <date> date change to <str> date ('YYYYMMDD')
        v_day, v_month, v_year = DateUtils().get_variables_from_date(v_date)
        self.new_file_dt = DateUtils.set_variables_to_date(v_day, v_month, v_year)
        self.new_file_dt = DateUtils.add_days_to_date(self.new_file_dt, 1)
        self.new_file_dt = DateUtils.date_to_string(self.new_file_dt)

    def change_file_nm(self, v_date):
        # 1. from <str> date ('YYYY-MM-DD'), set new file_nm -> set_new_file_nm()
        # 2. replace old nm to new nm
        # 3. replace old file nm to new file nm
        # 4. return new file nm
        self.set_new_file_dt(v_date)
        v_new_file_nm = self.file_nm.replace(self.file_dt, self.new_file_dt)
        v_new_file_path = os.path.join(self.dir, v_new_file_nm)

        os.rename(self.file_path, v_new_file_path)
        file_log.info(f'File name was changed from: {self.file_path} to {v_new_file_path}')
        return v_new_file_nm
