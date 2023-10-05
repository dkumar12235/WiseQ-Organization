import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_Driver import BaseDriver

class CreateMentor(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.mentor_XPATH = "(//span[@class='menu-text'][normalize-space()='Mentors'])[2]"
        self.add_mentor_xpath = "(//div[@class='btn px-15 btn-primary'])[1]"
        self.enter_eid_xpath = "//input[@placeholder='EID']"
        self.enter_email_xpath = "//input[@placeholder='Email']"
        self.enter_first_name_xpath = "//input[@placeholder='First Name']"
        self.enter_last_name_xpath = "//input[@placeholder='Last Name']"
        self.enter_job_title_xpath = "//input[@placeholder='Job Title']"
        self.select_functional_area_xpath = "//select[@name='functionalArea']"
        self.enter_years_with_company_xpath = "//input[@placeholder='Years with the Company']"
        self.select_level_of_emp_xpath = "//select[@name='levelOfEmp']"
        self.select_work_location_xpath = "//select[@name='workLocation']"
        self.select_division_xpath = "//select[@name='division']"
        self.enter_reporting_manager_xpath = "//input[@placeholder='Reporting Manager Name']"
        self.enter_reporting_manager_eid_xpath = "//input[@placeholder='Reporting Manager EID']"
        self.select_country_xpath = "//select[@name='country']"
        self.submit_add_button_xpath = "//button[@type='submit']"
        self.click_on_delete_button_xpath = "//button[@type='button']"
        self.click_on_add_more_button_xpath = "(//p[@class='color-orange fw-500 mb-0'])[1]"
        self.click_on_upload_csv_file_xpath = "//a[normalize-space()='Upload CSV File']"
        self.click_to_download_csv_sample_file_xpath = "(//button[normalize-space()='Download Sample File'])[1]"
        self.click_to_close_model_xpath = "//button[@aria-label='Close']"

    def click_mentor(self):
        self.driver.find_element(By.XPATH, self.mentor_XPATH).click()

    def click_on_add_mentor(self):
        self.driver.find_element(By.XPATH, self.add_mentor_xpath).click()

    def enter_eid(self, eid):
        self.driver.find_element(By.XPATH, self.enter_eid_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_eid_xpath).send_keys(eid)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.enter_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_email_xpath).send_keys(email)

    def enter_first_name(self, fname):
        self.driver.find_element(By.XPATH, self.enter_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_first_name_xpath).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(By.XPATH, self.enter_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_last_name_xpath).send_keys(lname)

    def enter_job_title(self, jobtitle):
        self.driver.find_element(By.XPATH, self.enter_job_title_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_job_title_xpath).send_keys(jobtitle)

    def select_functional_area(self, value):
        dropdown = self.driver.find_element(By.XPATH, self.select_functional_area_xpath)
        dd = Select(dropdown)
        dd.select_by_value(value)

    def enter_year_with_company(self, yearwithcmpy):
        self.driver.find_element(By.XPATH, self.enter_years_with_company_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_years_with_company_xpath).send_keys(yearwithcmpy)

    def select_empy_level(self, value):
        dropdown = self.driver.find_element(By.XPATH, self.select_level_of_emp_xpath)
        dd = Select(dropdown)
        dd.select_by_value(value)

    def select_work_location(self, value):
        dropdown = self.driver.find_element(By.XPATH, self.select_work_location_xpath)
        dd = Select(dropdown)
        dd.select_by_value(value)

    def select_division(self, value):
        dropdown = self.driver.find_element(By.XPATH, self.select_division_xpath)
        dd = Select(dropdown)
        dd.select_by_value(value)

    def enter_reporting_manager_name(self, reportmangname):
        self.driver.find_element(By.XPATH, self.enter_reporting_manager_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_reporting_manager_xpath).send_keys(reportmangname)

    def enter_reporting_manager_eid(self, managereid):
        self.driver.find_element(By.XPATH, self.enter_reporting_manager_eid_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_reporting_manager_eid_xpath).send_keys(managereid)

    def select_country(self, value):
        dropdown = self.driver.find_element(By.XPATH, self.select_country_xpath)
        dd = Select(dropdown)
        dd.select_by_value(value)

    def add_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_add_button_xpath).click()

    def click_on_upload_csv_file(self):
        self.driver.find_element(By.XPATH, self.click_on_upload_csv_file_xpath).click()

    def click_to_download_csv_sample_file(self):
        self.driver.find_element(By.XPATH, self.click_to_download_csv_sample_file_xpath).click()

    def click_to_close_model(self):
        self.driver.find_element(By.XPATH, self.click_to_close_model_xpath).click()