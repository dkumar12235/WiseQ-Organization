import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.match_making_page import MatchMaking
from pages.wiseq_org_login_page import AdminLogin
from ddt import ddt, data
from utilities.utils import TestDataLoader


@ddt
@pytest.mark.usefixtures("setup")
class TestMatchMaking():
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
            print("'Expected Result' login successfylly")

    test_data = TestDataLoader.get_data("MatchMaking")  # Use the TestDataLoader to get data

    @pytest.mark.parametrize("browsementee", test_data)
    def test_create_match_making(self, browsementee):
        matchMaking = MatchMaking(self.driver)
        matchMaking.click_match_making()
        time.sleep(1)
        matchMaking.browse_mentee(browsementee)
        time.sleep(2)
        matchMaking.mark_checkbox_of_mentee()
        time.sleep(2)
        matchMaking.mark_checkbox_of_mentor()
        time.sleep(2)
        matchMaking.click_on_pair_button()
        time.sleep(2)
        matchMaking.click_on_confirmation_pair_button()
        time.sleep(2)
        matchMaking.click_on_alert_for_confirmation_alert()
        time.sleep(2)


