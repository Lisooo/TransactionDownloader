from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from transactions_downloader.locators import UserPassPageLocators, HomePageLocators
from transactions_downloader.utils import DateUtils, TimeUtils


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        self.delay = WebDriverWait(driver, 30, ignored_exceptions=self.ignored_exceptions)

    def click_element_xpath(self, element_xpath):
        # Another element is covering the element you are to click. You could use execute_script() to click on this.
        self.delay.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        try:
            element = self.driver.find_element(By.XPATH, element_xpath)
            self.driver.execute_script("arguments[0].click();", element)
        except StaleElementReferenceException:
            element = self.driver.find_element(By.XPATH, element_xpath)
            self.driver.execute_script("arguments[0].click();", element)

    def click_element_result(self, element_xpath):
        try:
            self.driver.find_element(By.XPATH, element_xpath)
            return True
        except:
            return False

    def clear_element_xpath(self, element_xpath):
        self.delay.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        self.driver.find_element(By.XPATH, element_xpath).clear()

    def sendkeys_element_xpath(self, element_xpath, userpass):
        self.delay.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        self.driver.find_element(By.XPATH, element_xpath).send_keys(userpass)

    def get_attr_from_xpath(self, attr, xpath):
        self.delay.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element = self.driver.find_element(By.XPATH, xpath)
        attr = element.get_attribute(attr)
        return attr


class UserPassPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = UserPassPageLocators

    def enter_login_param(self, param):
        self.clear_element_xpath(self.locators.userpass_textbox_xpath)
        self.sendkeys_element_xpath(self.locators.userpass_textbox_xpath, param)

    def click_next_button(self):
        self.click_element_xpath(self.locators.next_button_xpath)

    def click_login_button(self):
        self.click_element_xpath(self.locators.login_button_xpath)

    def login(self, user, password):
        self.enter_login_param(user)
        TimeUtils.wait_x_sec(1)
        self.click_next_button()
        TimeUtils.wait_x_sec(1)
        self.enter_login_param(password)
        TimeUtils.wait_x_sec(1)
        self.click_login_button()


class HomePage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators

    def click_history_link(self):
        self.click_element_xpath(self.locators.history_link_xpath)

    def get_date_from_input(self, v_fieldtype):
        if v_fieldtype == 1:
            v_input_date = self.get_attr_from_xpath("value", self.locators.dateTo_xpath)
        elif v_fieldtype == 2:
            v_input_date = self.get_attr_from_xpath("value", self.locators.dateFrom_xpath)
        else:
            print("Błędny V_FIELDTYPE: " + str(v_fieldtype))
            quit()

        return v_input_date

    def click_input_field(self, v_day, v_month, v_year, v_fieldtype):
        if v_fieldtype == 1:
            print("Wprowadzam datę DO: " + str(v_day) + "-" + str(v_month) + "-" + str(v_year))
            self.click_element_xpath(self.locators.dateTo_xpath)
        elif v_fieldtype == 2:
            print("Wprowadzam datę OD: " + str(v_day) + "-" + str(v_month) + "-" + str(v_year))
            self.click_element_xpath(self.locators.dateFrom_xpath)
        else:
            print("Błędny V_FIELDTYPE: " + str(v_fieldtype))
            quit()

    def set_date_into_input_field(self, v_day, v_month, v_year, v_fieldtype):
        v_input_date = self.get_date_from_input(v_fieldtype)

        v_month_name = DateUtils.get_month_name_from_dict(v_month)
        v_input_year = DateUtils.get_year_from_date(v_input_date)
        v_input_month = DateUtils.get_month_from_date(v_input_date)

        l_oday_xpath = self.locators.day_xpath(v_day)
        l_year_text_xpath = self.locators.year_text_xpath(v_year)
        l_date_text_xpath = self.locators.date_text_xpath(v_month_name, v_year)

        year_rslt = self.click_element_result(l_year_text_xpath)
        if int(v_year) == int(v_input_year):
            date_rslt = self.click_element_result(l_date_text_xpath)
            while date_rslt is False:
                if int(v_month) < int(v_input_month):
                    self.click_element_xpath(self.locators.prevMonth_xpath)
                    TimeUtils.wait_x_sec(2)
                else:
                    self.click_element_xpath(self.locators.nextMonth_xpath)
                    TimeUtils.wait_x_sec(2)

                date_rslt = self.click_element_result(l_date_text_xpath)
            else:
                self.click_element_xpath(l_oday_xpath)

        if int(v_year) > int(v_input_year):
            while year_rslt is False:
                self.click_element_xpath(self.locators.nextMonth_xpath)
                year_rslt = self.click_element_result(l_year_text_xpath)
            else:
                date_rslt = self.click_element_result(l_date_text_xpath)
                while date_rslt is False:
                    if int(v_month) < int(v_input_month):
                        self.click_element_xpath(self.locators.prevMonth_xpath)
                    else:
                        self.click_element_xpath(self.locators.nextMonth_xpath)
                    date_rslt = self.click_element_result(l_date_text_xpath)
                else:
                    self.click_element_xpath(l_oday_xpath)

        if int(v_year) < int(v_input_year):
            while year_rslt is False:
                self.click_element_xpath(self.locators.prevMonth_xpath)
                year_rslt = self.click_element_result(l_year_text_xpath)
            else:
                date_rslt = self.click_element_result(l_date_text_xpath)
                while date_rslt is False:
                    if int(v_month) < int(v_input_month):
                        self.click_element_xpath(self.locators.nextMonth_xpath)
                    else:
                        self.click_element_xpath(self.locators.prevMonth_xpath)
                    date_rslt = self.click_element_result(l_date_text_xpath)
                else:
                    self.click_element_xpath(l_oday_xpath)

    def set_date_input(self, v_day, v_month, v_year, v_fieldtype):
        self.click_input_field(v_day, v_month, v_year, v_fieldtype)
        self.set_date_into_input_field(v_day, v_month, v_year, v_fieldtype)

    def download_file(self, file_format):
        rslt = self.click_element_result(self.locators.no_results_div_xpath)
        if rslt is False:
            self.click_element_xpath(self.locators.download_xpath)
            self.click_element_xpath(self.locators.file_format_xpath(file_format))
            return True, ' '
        else:
            return False, 'There was no transaction on that day'
