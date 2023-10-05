import time

from selenium.webdriver.common.by import By


class Home_Dashboard():
    def __init__(self, driver):
        self.driver = driver
        self.Mentoring_hours_xpath = "//p[normalize-space()='Mentoring Hours']"
        self.Mentees_active_xpath = "//p[normalize-space()='Mentees']"
        self.Mentors_active_xpath = "//p[normalize-space()='Mentors']"
        self.Average_impact_score_xpath = "//p[normalize-space()='Avg. Impact Score']"
        self.Session_completed_xpath = "//p[normalize-space()='Sessions Completed']"
        self.Growth_credits_xpath = "//p[normalize-space()='Growth Credits']"
        self.homepage_XPATH = "//div[@id='sidebar']//div//span[contains(text(),'Home')]"

    def click_mentoring_hours(self):
        self.driver.find_element(By.XPATH, self.Mentoring_hours_xpath).click()
    def click_active_mentees(self):
        self.driver.find_element(By.XPATH, self.Mentees_active_xpath).click()
    def click_active_mentors(self):
        self.driver.find_element(By.XPATH, self.Mentors_active_xpath).click()
    def click_average_impact_score(self):
            self.driver.find_element(By.XPATH, self.Average_impact_score_xpath).click()
    def click_session_completed(self):
        self.driver.find_element(By.XPATH, self.Session_completed_xpath).click()
    def click_growth_credits(self):
        self.driver.find_element(By.XPATH, self.Growth_credits_xpath).click()
    def click_homepage(self):
        self.driver.find_element(By.XPATH, self.homepage_XPATH).click()





