class UserPassPageLocators(object):
    userpass_textbox_xpath = ".//*[contains(@name,'LOGIN')]"
    next_button_xpath = ".//button/span[text()='Dalej']"
    login_button_xpath = ".//button/span[text()='Zaloguj']"


class HomePageLocators(object):
    # history_link_xpath = ".//a[text()='wszystkie operacje']" #OLD VERSION BCKP
    history_link_xpath = ".//span[text()='Historia']"
    dateFrom_xpath = ".//input[contains(@name,'dateFrom')]"
    dateTo_xpath = ".//input[contains(@name,'dateTo')]"
    download_xpath = ".//div[text()='Pobierz']"
    no_results_div_xpath = ".//div[text()[contains(.,'Brak wyników')]]"
    nextMonth_xpath = ".//button/span[text()='Następny miesiąc']"
    prevMonth_xpath = ".//button/span[text()='Poprzedni miesiąc']"
    nextYear_xpath = ".//button/span[text()='Następny rok']"
    prevYear_xpath = ".//button/span[text()='Poprzedni rok']"

    @staticmethod
    def file_format_xpath(v_file_format):
        v_file_format = str(v_file_format)
        file_format_xpath = ".//div/a[text()=" + v_file_format + "]"
        return file_format_xpath

    @staticmethod
    def date_text_xpath(v_month, v_year):
        v_month = str(v_month)
        v_year = str(v_year)
        date_text_xpath = ".//div[@class!='last_login' and @class!='copyright' and text()[contains(.,'" + v_month + \
                          " " + v_year + "')]]"
        return date_text_xpath

    @staticmethod
    def day_xpath(v_day):
        v_day = str(v_day)
        day_xpath = ".//div/label/div[text()=" + v_day + "]"
        return day_xpath

    @staticmethod
    def year_text_xpath(v_year):
        v_year = str(v_year)
        year_text_xpath = ".//div[@class!='last_login' and @class!='copyright' " \
                          "and text()[contains(.,'" + v_year + "')]]"
        return year_text_xpath

    @staticmethod
    def month_name_xpath(v_month_name):
        v_month_name = str(v_month_name)
        mont_name_xpath = ".//div[text()[contains(.,'" + v_month_name + "')]]"
        return mont_name_xpath
