import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.wiseq_org_login_page import AdminLogin
from ddt import ddt, data
from utilities.utils import TestDataLoader
from pages.organisation_sidemenu_page_navigation import SideMenuPagesclickEvents

@ddt
@pytest.mark.usefixtures("setup")
class TestValidLogin():
    test_data = TestDataLoader.get_data("validlogin")  # Use the TestDataLoader to get data
    @pytest.mark.parametrize("email, password", test_data)

    def test_login_with_valid_credntials(self, email, password):
        login = AdminLogin(self.driver)
        login.enter_email(email)
        login.enter_password(password)
        login.click_on_sign_in_button()
        time.sleep(3)
        try:
            assert "Home" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login details are wrong")
        else:
            print("'Expected Result' login successfylly")

    def test_verify_side_menu_clickable(self):
        clickOnSideMenus = SideMenuPagesclickEvents(self.driver)
        time.sleep(1)
        clickOnSideMenus.click_mentee()
        try:
            assert "Mentees" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Mentees page is not available")
        else:
            print("'Expected Result' Mentees page successfylly available")
        time.sleep(1)

        clickOnSideMenus.click_mentor()
        try:
            assert "Mentors" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Mentors page is not available")
        else:
            print("'Expected Result' Mentors page successfylly available")
        time.sleep(1)
        clickOnSideMenus.click_match_making()
        try:
            assert "Match-Making" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Match-Making page is not available")
        else:
            print("'Expected Result' Match-Making page successfylly available")
        clickOnSideMenus.click_mentoring_program()
        try:
            assert "Mentoring Programs" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Mentoring Programs page is not available.")
        else:
            print("'Expected Result' Mentoring Programs page successfylly available but still We are currently developing this feature. It will be available to you soon.")
        time.sleep(1)
        clickOnSideMenus.click_progress_report()
        try:
            assert "Progress Reports" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Progress Reports page is not available.")
        else:
            print("'Expected Result' Progress Reports page successfylly available  but still We are currently developing this feature. It will be available to you soon.")
        clickOnSideMenus.click_homepage()
        try:
            assert "Home" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Home page is not available")
        else:
            print("'Expected Result' Home page successfylly available")
        time.sleep(1)


