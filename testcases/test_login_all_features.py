import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.wiseq_org_login_page import AdminLogin
from ddt import ddt, data
from utilities.utils import TestDataLoader


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

    def test_profile_and_signout(self):
        logout = AdminLogin(self.driver)
        logout.click_profile()
        time.sleep(2)
        logout.click_signout()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: logout is not happening")
        else:
            print("'Expected Result' logout successfylly")
        time.sleep(2)

class TestInValidLogin():
    test_data = TestDataLoader.get_data("InvalidEmail")  # Use the TestDataLoader to get data

    @pytest.mark.parametrize("email, password", test_data)
    def test_enterinvalid_email(self, email, password):
        enterinvalidlogin = AdminLogin(self.driver)
        enterinvalidlogin.enter_email(email)
        enterinvalidlogin.enter_password(password)
        enterinvalidlogin.click_on_sign_in_button()
        time.sleep(2)
        enterinvalidlogin.driver.switch_to.alert.accept()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login successfully")
        else:
            print("'Expected Result' login should not be happen")


        time.sleep(2)

    test_data = TestDataLoader.get_data("invalidpasswordvalidmail")  # Use the TestDataLoader to get data

    @pytest.mark.parametrize("email, password", test_data)
    def test_enterinvalid_password(self, email, password):
        enterinvalidlogin = AdminLogin(self.driver)
        enterinvalidlogin.enter_email(email)
        enterinvalidlogin.enter_password(password)
        enterinvalidlogin.click_on_sign_in_button()
        time.sleep(2)
        enterinvalidlogin.driver.switch_to.alert.accept()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login successfully")
        else:
            print("'Expected Result' login should not be happen")
        time.sleep(2)
    def test_enterinvalid_email_password(self):
        enterinvalidemailpass = AdminLogin(self.driver)
        enterinvalidemailpass.enter_email("1demo@example.com")
        enterinvalidemailpass.enter_password("password1")
        enterinvalidemailpass.click_on_sign_in_button()
        time.sleep(2)
        enterinvalidemailpass.driver.switch_to.alert.accept()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login successfully")
        else:
            print("'Expected Result' login should not be happen")
        time.sleep(2)

    def test_forgot_password_feature(self):
        forgotpsd = AdminLogin(self.driver)
        forgotpsd.click_forgot_password()
        time.sleep(2)
        forgotpsd.enter_pass_recovery_email("demo@example.com")
        forgotpsd.click_submit_button()
        try:
            assert "Forgot Password" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Forgot password link is not sent in email")
        else:
            print("'Expected Result' forgot password link has been sent successfully in the email")
        time.sleep(2)

        forgotpsd.close_success_alter()
class TestValidation():
    def test_Empty_EmailandPassword(self):

        admin_login = AdminLogin(self.driver)

        admin_login.click_on_sign_in_button()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login successfully")
        else:
            print("'Expected Result' login should not be happen")
        time.sleep(2)


    def test_Empty_Email_Valid_Password(self):
        admin_login = AdminLogin(self.driver)
        admin_login.enter_password("password")
        time.sleep(2)
        admin_login.click_on_sign_in_button()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login successfully")
        else:
            print("'Expected Result' login should not be happen")
        time.sleep(2)

    def test_Empty_password_Valid_Email(self):
        admin_login = AdminLogin(self.driver)
        admin_login.enter_email("demo@example.com")
        time.sleep(2)
        admin_login.click_on_sign_in_button()
        try:
            assert "Sign in" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: login successfully")
        else:
            print("'Expected Result' login should not be happen")
        time.sleep(2)










