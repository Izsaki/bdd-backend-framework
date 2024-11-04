from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from utils.frontend.pages.BasePage import BasePage
from utils.frontend.pages.MoreInfoPage import MoreInfoPage


class FrontPage(BasePage):
    header:WebElement
    more_info:WebElement

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def init_elements(self):
        self.header = self.find_element("body > div > h1")
        self.more_info = self.find_element("body > div > p:nth-child(3) > a")

    def open_homepage(self):
        self.open(self.base_url)
        self.init_elements()

    def open_more_info(self) -> MoreInfoPage:
        self.click_on_element(self.more_info)
        self.driver.implicitly_wait(5)
        return MoreInfoPage(driver=self.driver, url=self.driver.current_url)





