import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_bdd import given, scenarios, when, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from config.TestConfig import TestConfig
from utils.frontend.pages.Frontpage import FrontPage
from utils.frontend.pages.MoreInfoPage import MoreInfoPage

scenarios("../feature/selenium_frontend.feature")
test_config = TestConfig()

@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    pytest.driver = driver
    yield driver
    driver.quit()
    
@given("I open a browser")
def open_browser(chrome_driver):
    frontpage = FrontPage(chrome_driver, test_config.frontend_url)
    pytest.frontpage = frontpage
    frontpage.open_homepage()

@when("I click on More Information")
def click_more_information():
    frontpage:FrontPage
    frontpage = pytest.frontpage
    pytest.moreinfo_page = frontpage.open_more_info()

@then("more info page should be opened")
def check_moreinfo_page():
    driver:WebDriver
    driver = pytest.driver
    more_info_page:MoreInfoPage
    more_info_page = pytest.moreinfo_page
    allure.attach(pytest.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert more_info_page.logo is not None
    assert more_info_page.title.text == "Example Domains"

