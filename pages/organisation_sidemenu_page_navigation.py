import time

from selenium.webdriver.common.by import By


class SideMenuPagesclickEvents():
    def __init__(self, driver):
        self.driver = driver
        self.homepage_XPATH = "//div[@id='sidebar']//div//span[contains(text(),'Home')]"
        self.mentee_XPATH = "//ul[@class='sidebar_nav']//span[@class='menu-text'][normalize-space()='Mentees']"
        self.mentor_XPATH = "(//span[@class='menu-text'][normalize-space()='Mentors'])[2]"
        self.match_making_XPATH = "(//span[@class='menu-text'][normalize-space()='Match-Making'])[2]"
        self.mentoring_program_XPATH = "(//span[@class='menu-text'][normalize-space()='Mentoring Programs'])[2]"
        self.progress_report_XPATH = "(//span[@class='menu-text'][normalize-space()='Progress Reports'])[2]"


    def click_homepage(self):
        self.driver.find_element(By.XPATH, self.homepage_XPATH).click()

    def click_mentee(self):
        self.driver.find_element(By.XPATH, self.mentee_XPATH).click()
    def click_mentor(self):
        self.driver.find_element(By.XPATH, self.mentor_XPATH).click()
    def click_match_making(self):
        self.driver.find_element(By.XPATH, self.match_making_XPATH).click()
    def click_mentoring_program(self):
        self.driver.find_element(By.XPATH, self.mentoring_program_XPATH).click()
    def click_progress_report(self):
        self.driver.find_element(By.XPATH, self.progress_report_XPATH).click()



