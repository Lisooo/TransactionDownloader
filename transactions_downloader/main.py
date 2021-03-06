from transactions_downloader.pages import UserPassPage, HomePage
from transactions_downloader.drivers import FirefoxDriver
from transactions_downloader.import_log.utils import ImportLog
from transactions_downloader.connections import HomeBudgetConnection
from transactions_downloader.files.utils import FileUtils
from transactions_downloader.loggers import Logger

#   SETTING/INITIATE PHASE
logger = Logger('Main').logger()
logger.info(f'Started'.upper())

connection = HomeBudgetConnection().set()   # setting instance for db connection
cursor = connection.cursor()    # setting cursor to db operations

import_log = ImportLog(cursor)  # setting instance for ImportLog

driver = FirefoxDriver().setup()    # initiate driver
userpassPage = UserPassPage(driver)
homePage = HomePage(driver)

userpassPage.login()    # login
homePage.click_history_link()  # click History Link

for str_date in import_log.generate_date_list_to_download():

    #   setting dateFrom and dateTO in website
    #   1 - dateTo; 2 - dateFrom
    homePage.set_date_input(str_date, 1)  # set dateTo
    homePage.set_date_input(str_date, 2)  # set dateFrom

    v_status, v_msg = homePage.download_file()  # download file to specified location and receive result
    if v_status is True:
        v_new_file_nm = FileUtils().change_file_nm(str_date)  # setting instance for File

        #   Insert into IMPORT_CSV
        import_log.insert_into_import_log(v_new_file_nm, str_date, v_msg, 'N', 'N')
        connection.commit()

    else:
        import_log.insert_into_import_log('', str_date, v_msg, ' ', ' ')
        connection.commit()

logger.info(f'Ended successful'.upper())
driver.close()
driver.quit()
