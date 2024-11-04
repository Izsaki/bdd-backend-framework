from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    driver:WebDriver

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator: str) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, locator[0])

    def wait_for_element(self, *locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR))

    def click_on_element(self, *locator):
        WebDriver.find_element(self.driver, locator).click()

    def click_on_element(self, element: WebElement):
        element.click()

