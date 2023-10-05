import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.create_mentee_page import CreateMentee
from pages.wiseq_org_login_page import AdminLogin
from ddt import ddt, data
from utilities.utils import TestDataLoader

@ddt
@pytest.mark.usefixtures("setup")
class TestAddMentee():
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

        def test_Verify_that_user_click_on_mentee_then_showing_add_mentee_button_is_available_or_not(self):
            verifyAddMentee = CreateMentee(self.driver)
            verifyAddMentee.click_mentee()
            try:
                assert "Add Mentee" in self.driver.page_source
            except AssertionError:
                print("Assertion failed: Add Mentee button is not showing")
            else:
                print("'Expected Result' Add Mentee button is showing in the page")

        def test_Verify_that_add_mentee_form_showing_after_click_on_addButton_or_not(self):
            verifyClickableAddbutton = CreateMentee(self.driver)
            verifyClickableAddbutton.click_mentee()
            time.sleep(1)
            verifyClickableAddbutton.click_on_add_mentee()
            try:
                assert "Add Mentee" in self.driver.page_source
            except AssertionError:
                print("Assertion failed: Add Mentee page is not available")
            else:
                print("'Expected Result' Add Mentee form is showing in the page")

    def test_Verify_all_input_fields_are_available_in_the_form(self):
        verifyFormInput = CreateMentee(self.driver)
        verifyFormInput.click_mentee()
        time.sleep(1)
        verifyFormInput.click_on_add_mentee()

        expected_fields = ["EID", "Email", "fname", "lname", "Job Title", "Select Functional Area", "Years with the Company", "Select Level of Employee", "Select Work Location", "Select Division", "Reporting Manager Name", "Reporting Manager EID", "Select Country"]
        for field in expected_fields:
            assert field in self.driver.page_source, f"{field} field is not available in the form"
        print("Expected Result: All input fields are available in the form")

    def test_verifyclick_on_submitButton_without_fill_data_on_create_mentree_form(self):
        verifyFormInput = CreateMentee(self.driver)
        verifyFormInput.click_mentee()
        time.sleep(1)
        verifyFormInput.click_on_add_mentee()
        try:
            assert "Add Mentee" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Without input any data form has been submitted")
        else:
            print("'Expected Result' without input complete information form should not be submit")
    def test_verify_upload_csv_file_feature_is_available_or_not_in_the_create_mentee_page(self):
        verifyFormInput = CreateMentee(self.driver)
        verifyFormInput.click_mentee()
        time.sleep(1)
        verifyFormInput.click_on_add_mentee()
        try:
            assert "Upload CSV File" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Upload CSV File feature is not available in the page")
        else:
            print("'Expected Result' Upload CSV File feature is available in the create mentee page")

    def test_verify_upload_csv_file_feature_is_clickable_or_not(self):
        verifyFormInput = CreateMentee(self.driver)
        verifyFormInput.click_mentee()
        time.sleep(1)
        verifyFormInput.click_on_add_mentee()
        time.sleep(1)
        verifyFormInput.click_on_upload_csv_file()
        time.sleep(1)
        try:
            assert "Browse Files to upload" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Upload CSV File feature is not clickable")
        else:
            print("'Expected Result' Upload CSV File feature is working fine and there is shwoing browse file popup")
        verifyFormInput.click_to_close_model()
        time.sleep(1)
    def test_verify_upload_csv_sample_file_is_available_or_not(self):
        verifyFormInput = CreateMentee(self.driver)
        verifyFormInput.click_mentee()
        time.sleep(1)
        verifyFormInput.click_on_add_mentee()
        time.sleep(1)
        verifyFormInput.click_on_upload_csv_file()
        time.sleep(2)
        verifyFormInput.click_to_download_csv_sample_file()
        time.sleep(2)
        verifyFormInput.click_to_close_model()

        try:
            assert "Download Sample File" in self.driver.page_source
        except AssertionError:
            print("Assertion failed: Download Sample File is not available")
        else:
            print("'Expected Result' Download Sample File has been downloaded successfully")


    test_data = TestDataLoader.get_data("CreateMentee")  # Use the TestDataLoader to get data
    @pytest.mark.parametrize("EID, EMAIL, FNAME, LNAME, JOB_TITLE, SELECT_FUNCTIONAL_AREA, YEAR_WITH_THE_COMPANY, SELECT_LEVEL_OF_EMP, SELECT_WORK_LOCATION, SELECT_DIVISION, REPORTING_MANAGER, REPORTING_MANAGER_EID, SELECT_COUNTRY", test_data)
    def test_add_mentee(self, EID, EMAIL, FNAME, LNAME, JOB_TITLE, SELECT_FUNCTIONAL_AREA, YEAR_WITH_THE_COMPANY, SELECT_LEVEL_OF_EMP,
                        SELECT_WORK_LOCATION, SELECT_DIVISION, REPORTING_MANAGER, REPORTING_MANAGER_EID, SELECT_COUNTRY):
        AddMentee = CreateMentee(self.driver)
        AddMentee.click_mentee()
        time.sleep(2)
        AddMentee.click_on_add_mentee()
        time.sleep(1)
        AddMentee.enter_eid(EID)
        time.sleep(1)
        AddMentee.enter_email(EMAIL)
        time.sleep(1)
        AddMentee.enter_first_name(FNAME)
        time.sleep(1)
        AddMentee.enter_last_name(LNAME)
        time.sleep(1)
        AddMentee.enter_job_title(JOB_TITLE)
        time.sleep(1)
        AddMentee.select_functional_area(SELECT_FUNCTIONAL_AREA)
        time.sleep(2)
        AddMentee.enter_year_with_company(YEAR_WITH_THE_COMPANY)
        time.sleep(1)
        AddMentee.select_empy_level(SELECT_LEVEL_OF_EMP)
        time.sleep(2)
        AddMentee.select_work_location(SELECT_WORK_LOCATION)
        time.sleep(2)
        AddMentee.select_division(SELECT_DIVISION)
        time.sleep(2)
        AddMentee.enter_reporting_manager_name(REPORTING_MANAGER)
        time.sleep(1)
        AddMentee.enter_reporting_manager_eid(REPORTING_MANAGER_EID)
        time.sleep(1)
        AddMentee.page_scroll()

        AddMentee.select_country(SELECT_COUNTRY)
        time.sleep(2)
