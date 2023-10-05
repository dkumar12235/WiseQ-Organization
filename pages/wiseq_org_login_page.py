from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import time
class AdminLogin():
    def __init__(self, driver):
        self.driver = driver
        # self.wait = wait
        self.email_txtbox_XPATH = "(//input[@id='username'])[1]"
        self.passwrod_txtbox_name ="password"
        self.sign_button_XPATH = "//button[normalize-space()='sign in']"
        self.click_on_profile_XPATH = "(//img[@class='rounded-circle'])[1]"
        self.click_on_signout_XPATH = "//a[normalize-space()='Sign Out']"
        self.forgot_passwrod_XPATH = "//a[normalize-space()='forgot password?']"
        self.enter_recovery_password_email_XPATH = "//input[@id='username']"
        self.forgot_submit_button_XPATH = "//button[normalize-space()='Submit']"
        self.success_alert_XPATH = "//button[@aria-label='Close']"

    def enter_email(self, username):
        self.driver.find_element(By.XPATH, self.email_txtbox_XPATH).clear()
        self.driver.find_element(By.XPATH, self.email_txtbox_XPATH).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.passwrod_txtbox_name).clear()
        self.driver.find_element(By.NAME, self.passwrod_txtbox_name).send_keys(password)
    def click_on_sign_in_button(self):
        self.driver.find_element(By.XPATH, self.sign_button_XPATH).click()
    def click_profile(self):
        self.driver.find_element(By.XPATH, self.click_on_profile_XPATH).click()
    def click_signout(self):
        self.driver.find_element(By.XPATH, self.click_on_signout_XPATH).click()

    # forgot password feature
    def click_forgot_password(self):
        self.driver.find_element(By.XPATH, self.forgot_passwrod_XPATH).click()
    def enter_pass_recovery_email(self, forgotEmail):
        self.driver.find_element(By.XPATH, self.enter_recovery_password_email_XPATH).send_keys(forgotEmail)
    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.forgot_submit_button_XPATH).click()
    def close_success_alter(self):
        self.driver.find_element(By.XPATH, self.success_alert_XPATH).click()




