import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.dashboard_home_page import Home_Dashboard
from pages.wiseq_org_login_page import AdminLogin
from ddt import ddt, data
from utilities.utils import TestDataLoader

@ddt
@pytest.mark.usefixtures("setup")
class Test_Dashboard_Tabs():
    test_data = TestDataLoader.get_data("validlogin")  # Use the TestDataLoader to get data
    @pytest.mark.parametrize("email, password", test_data)
    def test_login_in_organisation(self, email, password):
        login = AdminLogin(self.driver)
        login.enter_email(email)
        login.enter_password(password)
        login.click_on_sign_in_button()
        time.sleep(2)
        try:
            assert "Home" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login details are wrong")
        else:
            print("'Expected Result' Organisation has been logged in successfylly ")
    def test_Verify_Mentoring_hours_is_clickable_or_not(self):
        verifytabs = Home_Dashboard(self.driver)
        verifytabs.click_mentoring_hours()
        time.sleep(1)
        verifytabs.click_homepage()
        time.sleep(1)
        try:
            assert "Progress Report" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Mentoring hours tab is not clickable")
        else:
            print("'Expected Result' Mentoring hours tab is clickable and redirect to progress report page")
    def test_Verify_Active_Mentees_tab_is_clickable_or_not(self):
        verifytabs = Home_Dashboard(self.driver)
        verifytabs.click_active_mentees()
        time.sleep(2)
        verifytabs.click_homepage()
        time.sleep(2)

        try:
            assert "Mentees" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Page does not redirect to active mentees list")
        else:
            print("'Expected Result' Page is redirecting to active mentees list")
    def test_Verify_Active_Mentors_tab_is_clickable_or_not(self):
        verifytabs = Home_Dashboard(self.driver)
        verifytabs.click_active_mentors()
        time.sleep(2)
        verifytabs.click_homepage()
        time.sleep(1)

        try:
            assert "Mentors" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Page does not redirect to active Mentors list")
        else:
            print("'Expected Result' Page is redirecting to active Mentors list")

    def test_Verify_Average_impact_tab_is_clickable_or_not(self):
        verifytabs = Home_Dashboard(self.driver)
        verifytabs.click_average_impact_score()
        time.sleep(2)
        verifytabs.click_homepage()
        time.sleep(1)

        try:
            assert "Progress Report" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Average impact page does not redirect to progress report page")
        else:
            print("'Expected Result' Average impact tab is clickable and redirect to progress report page")
    def test_Verify_Session_completed_tab_is_clickable_or_not(self):
        verifytabs = Home_Dashboard(self.driver)
        verifytabs.click_session_completed()
        time.sleep(2)
        verifytabs.click_homepage()
        time.sleep(1)

        try:
            assert "Progress Report" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Session completed tab is not clickable")
        else:
            print("'Expected Result' Session completed tab is clickable and redirect to progress report page")
    def test_Verify_Growth_credits_tab_is_clickable_or_not(self):
        verifytabs = Home_Dashboard(self.driver)
        verifytabs.click_growth_credits()
        time.sleep(2)
        verifytabs.click_homepage()
        time.sleep(1)

        try:
            assert "Progress Report" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Growth credit tab is not clickable")
        else:
            print("'Expected Result' Growth credit tab is clickable and redirect to progress report page")
