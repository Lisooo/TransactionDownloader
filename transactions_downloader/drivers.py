from transactions_downloader.params import FileParams, PageParams
from selenium import webdriver


class FirefoxDriver(object):

    def __init__(self):
        self.download_dir = FileParams.files_dir
        self.file_format = FileParams.file_format

    def profile(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference('browser.download.dir', self.download_dir)
        fp.set_preference('browser.download.folderList', 2)
        fp.set_preference('browser.helperApps.neverAsk.saveToDisk',
                          "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,"
                          "text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,"
                          "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream")
        fp.set_preference('pdf.disabled', True)
        return fp

    def setup(self):
        driver = webdriver.Firefox(firefox_profile=self.profile(),
                                   executable_path=r"./browser_drivers/geckodriver.exe",
                                   service_log_path=r"./browser_drivers/geckodriver.log")
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        driver.get(PageParams.login_page_lnk)
        return driver
