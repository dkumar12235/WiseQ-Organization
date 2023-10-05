import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_Driver import BaseDriver

class MatchMaking(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.match_making_XPATH = "(//span[@class='menu-text'][normalize-space()='Match-Making'])[2]"
        self.browse_mentee_xpath = "//input[@placeholder='Browse Mentees']"
        self.browse_mentor_xpath = "//input[@placeholder='Browse Mentors']"
        self.select_checkbox_xpath= "(//span[contains(text(),'Select')])[1]"
        self.select_checkbox_of_mentor_xpath = "(//input[@type='checkbox'])[2]"
        self.click_on_pair_button_xpath = "(//button[@type='button'][normalize-space()='Pair'])[1]"
        self.click_on_confirm_pair_button_xpath = "(//div[@class='btn px-15 btn-primary'])[1]"
        self.click_on_alert_for_confirmation_xpath = "//button[normalize-space()='Confirm Pair']"

    def click_match_making(self):
        self.driver.find_element(By.XPATH, self.match_making_XPATH).click()
    def browse_mentee(self, browsementee):
        self.driver.find_element(By.XPATH, self.browse_mentee_xpath).clear()
        self.driver.find_element(By.XPATH, self.browse_mentee_xpath).send_keys(browsementee)
    def mark_checkbox_of_mentee(self):
        self.driver.find_element(By.XPATH, self.select_checkbox_xpath).click()
    def mark_checkbox_of_mentor(self):
        self.driver.find_element(By.XPATH, self.select_checkbox_of_mentor_xpath).click()
    def click_on_pair_button(self):
        self.driver.find_element(By.XPATH, self.click_on_pair_button_xpath).click()
    def click_on_confirmation_pair_button(self):
        self.driver.find_element(By.XPATH, self.click_on_confirm_pair_button_xpath).click()
    def click_on_alert_for_confirmation_alert(self):
        self.driver.find_element(By.XPATH, self.click_on_alert_for_confirmation_xpath).click()





