from selenium.webdriver.remote.webelement import WebElement

from utils.frontend.pages.BasePage import BasePage


class MoreInfoPage(BasePage):
    logo:WebElement
    title:WebElement

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.init_elements()

    def init_elements(self):
        self.logo = self.find_element("#logo > a > img")
        self.title = self.find_element("#body > article > main > div > h1")