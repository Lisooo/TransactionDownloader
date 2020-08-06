from transactions_downloader import driver, p_csv_files_dir, p_curr_dttm, p_start_dt, p_password, p_login, p_file_format
from transactions_downloader.pages import UserPassPage, HomePage
from transactions_downloader.utils import DateUtils, TimeUtils, FileUtils, DBUtils

if __name__ == "__main__":
    print("HELLO")
    userpassPage = UserPassPage(driver)
    homePage = HomePage(driver)
    #
    #   GENERATE DATES to download
    file_list = FileUtils.get_files_list_from_dir(p_csv_files_dir)
    str_date_list = FileUtils.generate_date_list_to_download(p_start_dt, p_curr_dttm, file_list)

    # USERPASS -> LOGIN
    userpassPage.login(p_login, p_password)

    # HOMEPAGE -> HISTORY_LINK
    homePage.click_history_link()  # click History Link

    for v_str_date in str_date_list:

        #   preparing variables
        v_day, v_month, v_year = DateUtils.get_variables_from_str_date(v_str_date)
        v_operation_dt = DateUtils.set_variables_to_date(v_day, v_month, v_year)
        v_file_dt = DateUtils.add_days_to_date(v_operation_dt, 1)

        #   setting dateFrom and dateTO in website
        #   1 - dateTo; 2 - dateFrom
        homePage.set_date_input(v_day, v_month, v_year, 1)  # set dateTo
        TimeUtils.wait_x_sec(2)
        homePage.set_date_input(v_day, v_month, v_year, 2)  # set dateFrom
        TimeUtils.wait_x_sec(2)

        status, msg = homePage.download_file(p_file_format)  # download file to specified location and receive result
        TimeUtils.wait_x_sec(2)

        if status is True:
            #   Variables for old file name
            v_old_file_nm = FileUtils.find_latest_file_nm(p_csv_files_dir)
            v_old_file_nm_dt = FileUtils.file_nm_into_str_date(v_old_file_nm)
            v_old_file_nm_path = FileUtils.set_filepath(p_csv_files_dir, v_old_file_nm)

            #   Variables for new file name
            v_new_file_dt = DateUtils.set_variables_to_date(v_day, v_month, v_year)
            v_new_file_dt = DateUtils.add_days_to_date(v_new_file_dt, 1)
            v_new_file_dt = DateUtils.date_to_string(v_new_file_dt)
            v_new_file_nm = v_old_file_nm.replace(v_old_file_nm_dt, v_new_file_dt)
            v_new_file_path = FileUtils.set_filepath(p_csv_files_dir, v_new_file_nm)

            #   Changing file name to new one
            FileUtils.change_file_nm(v_old_file_nm_path, v_new_file_path)

            #   Insert into IMPORT_CSV
            DBUtils.insert_into_import_log(v_new_file_nm, v_operation_dt, p_curr_dttm, msg, 'N', 'N')  # TMP

        else:
            print("There is no file for modify")
            DBUtils.insert_into_import_log('', v_operation_dt, p_curr_dttm, msg, ' ', ' ')     # TMP

    TimeUtils.wait_x_sec(5)
    driver.close()
    driver.quit()
