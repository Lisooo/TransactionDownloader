class UserPassPageLocators(object):
    userpass_textbox_xpath = ".//*[contains(@name,'LOGIN')]"
    next_button_xpath = ".//button/span[text()='Dalej']"
    login_button_xpath = ".//button/span[text()='Zaloguj']"


class HomePageLocators(object):

    history_link_xpath = ".//span[text()='Historia']"
    dateFrom_xpath = ".//input[contains(@name,'dateFrom')]"
    dateTo_xpath = ".//input[contains(@name,'dateTo')]"
    download_xpath = ".//div[text()='Pobierz']"
    no_results_div_xpath = ".//div[text()[contains(.,'Brak wyników')]]"
    nextMonth_xpath = ".//button/span[text()='Następny miesiąc']"
    prevMonth_xpath = ".//button/span[text()='Poprzedni miesiąc']"
    nextYear_xpath = ".//button/span[text()='Następny rok']"
    prevYear_xpath = ".//button/span[text()='Poprzedni rok']"
    myProductList_xpath = ".//button/span[text()='Moje produkty']"
    cardsList_xpath = ".//div/a[text()='Karty']"

    @staticmethod
    def file_format_xpath(v_file_format):
        return ".//div/a[text()=" + str(v_file_format) + "]"

    @staticmethod
    def date_text_xpath(v_month, v_year):
        return ".//div[@class!='last_login' and @class!='copyright' and text()[contains(.,'" + str(v_month) + \
                          " " + str(v_year) + "')]]"

    @staticmethod
    def day_xpath(v_day):
        return ".//div/label/div[text()=" + str(v_day) + "]"

    @staticmethod
    def year_text_xpath(v_year):
        return ".//div[@class!='last_login' and @class!='copyright' " \
                          "and text()[contains(.,'" + str(v_year) + "')]]"

    @staticmethod
    def month_name_xpath(v_month_nm):
        return ".//div[text()[contains(.,'" + str(v_month_nm) + "')]]"
