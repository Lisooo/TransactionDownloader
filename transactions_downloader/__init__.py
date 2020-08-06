from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from selenium import webdriver
from transactions_downloader.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# DB
db = SQLAlchemy(app)

# PARAMS
p_csv_files_dir = Config.CSV_FILES_DIR
p_start_dt = Config.START_DT
p_curr_dttm = Config.CURR_DATETIME
p_login = Config.USERNAME
p_password = Config.PASS
p_file_format = Config.CSV_FILE_FORMAT

# DRIVER
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.dir', p_csv_files_dir)
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.helperApps.neverAsk.saveToDisk',
                      "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream")
fp.set_preference('pdf.disabled', True)

driver = webdriver.Firefox(firefox_profile=fp,
                               executable_path=r"./browser_drivers/geckodriver.exe",
                               service_log_path=r"./browser_drivers/geckodriver.log")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get(Config.SITE_URL)
