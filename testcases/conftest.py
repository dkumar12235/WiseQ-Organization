import time
from datetime import datetime
from pathlib import Path

import pytest
import pytest_html
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



# DeprecationWarning: executable_path has - this method for remove this warning
@pytest.fixture(scope="class", autouse=True)
def setup(request):
# google chrome browser
# Create a Chrome browser instance
#     chrome_options = webdriver.ChromeOptions()
# Create a Service object using WebDriverManager
#     chrome_service = Service(ChromeDriverManager().install())
# Initialize the browser with the specified options and Service
#     driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # chrome_path = r"C:/Users/Appslure/PycharmProjects/WiseQ/drivers/chromedriver.exe"
    # service = Service(chrome_path)
    # driver = webdriver.Chrome(service=service)

# firefox browser
    geckodriver_path = r"D:/WiseQAutomation/WiseqOrganization/drivers/geckodriver.exe"
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service)
    # wait = WebDriverWait(driver, 10)
    driver.maximize_window()


    driver.get("https://wiseqglobal.com/admin")
    # yield it is a like of tear down methods
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(tryfirst=True)

def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("WiseQOrganisation_Reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Reports_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True
def pytest_html_report_title(report):
    report.title = "WiseQ Organisation Report"
